from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from advertisements.models import Advertisement


class UserSerializer(serializers.ModelSerializer):
    """Serializer для пользователя."""

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name',
                  'last_name',)


class AdvertisementSerializer(serializers.ModelSerializer):
    """Serializer для объявления."""

    creator = UserSerializer(
        read_only=True,
    )

    class Meta:
        model = Advertisement
        fields = ('id', 'title', 'description', 'creator',
                  'status', 'created_at',)

    def create(self, validated_data):
        """Метод для создания"""

        # Простановка значения поля создатель по-умолчанию.
        # Текущий пользователь является создателем объявления
        # изменить или переопределить его через API нельзя.
        # обратите внимание на `context` – он выставляется автоматически
        # через методы ViewSet.
        # само поле при этом объявляется как `read_only=True`
        validated_data["creator"] = self.context["request"].user
        print(validated_data)
        return super().create(validated_data)

    def validate(self, data):

        open_status = (len(Advertisement.objects.filter(creator=self.context["request"].user, status='OPEN')))
        if "status" not in data:
            if open_status == 10:
                raise ValidationError("у пользователя не может быть больше 10 открытых объявлений")

        if "status" in data:
            if data["status"] == "OPEN" and open_status == 10:
                raise ValidationError("у пользователя не может быть больше 10 открытых объявлений")

        """Метод   для валидации. Вызывается при создании и обновлении."""
        # TODO: добавьте требуемую валидацию
        return data
