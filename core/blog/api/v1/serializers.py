from  rest_framework import serializers
from ...models import Post, Category
from accounts.models import Profile



# class  PostSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=255)
    
class  CategorySerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Category
        fields =['id','name']

    
class  PostSerializer(serializers.ModelSerializer):
    snippet = serializers.ReadOnlyField(source="get_snippet")
    relative_url = serializers.URLField(source="get_absolute_api_url",
                                         read_only=True)
    absolute_url = serializers.SerializerMethodField()
    category = serializers.SlugRelatedField(many=False,
                                            slug_field="name", 
                                            queryset=Category.objects.all())
    # category = CategorySerializer()
    
    
    class Meta:
        model = Post
        # fields = "__all__"
        fields = ['id','title','author','image','category','content','snippet',
                 'relative_url','absolute_url','status','created_date','published_date']
        # read_only_fields = ['author', 'created_date', 'updated_date']
        read_only_fields = ['author']
    

    def create(self, validated_data):
        #     """
        #     Automatically set the author field to the currently authenticated user's profile.
        #     """
            # validated_data['author '] = Profile.objects.get(user = self.context.get('request').user.id)
        #     # validated_data['author'] = Profile.objects.get(user__id = self.context.get('request').user.id)
            # return super().create(validated_data)
            
            user = self.context['request'].user
            profile = Profile.objects.get(user=user)
            validated_data['author'] = profile  # Corrected key
            return super().create(validated_data)

    def get_absolute_url(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(obj.pk)
    
    #when we need to change data for show #
    def to_representation(self, instance):
        """
        Customize the data representation based on whether it's a single post or a list view.
        """
        request = self.context.get("request")
        # print(request.__dict__)
        rep =  super().to_representation(instance)
        
        # rep['state'] = 'list'
        # if request.parser_context.get("kwargs").get('pk'):
        #     rep['state'] = 'single'
        if request.parser_context.get("kwargs").get('pk'):
            # Single post view
            rep.pop('snippet', None)
            rep.pop('relative_url', None)
            rep.pop('absolute_url', None)
        else:
            # List view
            rep.pop('content', None)
            
        # Add detailed category data
        rep['category'] = CategorySerializer(instance.category,
                                              context={'request':request}).data
        return rep
    
   
            
        # def create(self, validated_data):
        #     user = self.context['request'].user
        #     try:
        #         profile = Profile.objects.get(user=user)  # Get the user's profile
        #     except Profile.DoesNotExist:
        #         raise serializers.ValidationError("The authenticated user does not have an associated profile.")
            
        #     validated_data['author'] = profile  # Assign the profile as the author
        #     return super().create(validated_data)

        