from accounts.models import Profile
from items.models import Image, Item
from likes.models import ImageLike, ItemLike

class TestingScript:

    ### likes ###
    def likes_script(self):
        username = 'Fuck'
        item_id = 3
        image_id = 1

        profile = Profile.objects.get(user=username)
        item = Item.objects.get(pk=item_id)
        image = Image.objects.get(pk=image_id)
        print(profile)
        print(item)
        print(image)

        # liking item
        print('does like item: ', ItemLike.objects.does_like(username, item_id, 'item'))
        itemlike = ItemLike(profile=profile, item=item)
        itemlike.save()
        print('liking item works: ', profile.item_likes.filter(item=item).exists())
        print('liked item: ', ItemLike.objects.does_like(username, item_id, 'item'))

        # liking image
        print('does like image: ', ImageLike.objects.does_like(username, item_id, 'image'))
        imagelike = ImageLike(profile=profile, item=image)
        imagelike.save()
        print('liking image works: ', profile.image_likes.filter(item=image).exists())
        print('liked item: ', ImageLike.objects.does_like(username, image_id, 'image'))

    ### comments ###
    def comments_script(self):
        pass

ts = TestingScript()
# ts.likes_script()
ts.comments_script()
