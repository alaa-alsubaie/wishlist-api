from rest_framework import serializers
from items.models import Item ,FavoriteItem
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', ]


class FavoriteItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteItem
        fields = '__all__'


class ItemListSerializer(serializers.ModelSerializer):

    fav_item = serializers.SerializerMethodField()

    detail = serializers.HyperlinkedIdentityField(
        view_name = "item-detail",
        lookup_field = "id",
        lookup_url_kwarg = "item_id"
        )


    added_by = UserSerializer()

    class Meta:
        model = Item
        fields = ['name', 'description','detail','added_by','fav_item',]

    def get_fav_item(self,obj):
        return obj.favoriteitem_set.count()

    

class ItemDetailSerializer(serializers.ModelSerializer):

    fav_item_list = serializers.SerializerMethodField()

    class Meta:
        model = Item
        fields = ['name','description','added_by','image','fav_item_list',]

    def get_fav_item_list(self,obj):
        return FavoriteItemSerializer(obj.fav_item_list_set.all(),many=True).data







