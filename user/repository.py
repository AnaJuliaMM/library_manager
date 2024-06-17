from .models import CustomUser

class CustomUserRepository:
    @staticmethod
    def get_all_users():
        return CustomUser.objects.all()

    @staticmethod
    def get_user_by_id(user_id):
        return CustomUser.objects.get(pk=user_id)

    @staticmethod
    def create_user(data):
        user = CustomUser.objects.create(
            name=data.get('name'),
            username=data.get('username'),
            email=data.get('email'),
            password=data.get('password')  
        )
        return user


    @staticmethod
    def update_user(user_instance, user_data):
        user_instance.name = user_data.get('name', user_instance.name)
        user_instance.username = user_data.get('username', user_instance.username)
        user_instance.email = user_data.get('email', user_instance.email)
        if 'password' in user_data:
            user_instance.set_password(user_data['password'])
        user_instance.save()
        return user_instance

    @staticmethod
    def delete_user(user_instance):
        user_instance.delete()

    @staticmethod
    def filter_user(filters):
        return CustomUser.objects.filter(**filters)
