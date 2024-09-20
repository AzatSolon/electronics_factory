from django.db import models

NULLABLE = {"blank": True, "null": True}


class Network(models.Model):
    LEVEL = (
        (0, "Завод"),
        (1, "Розничная сеть"),
        (2, "Индивидуальный предприниматель"),
    )

    name = models.CharField(max_length=100, verbose_name="Название")
    level = models.IntegerField(choices=LEVEL, verbose_name="Уровень поставщика")
    supplier = models.ForeignKey(
        "self", on_delete=models.CASCADE, verbose_name="Поставщик", **NULLABLE
    )
    debt_to_supplier = models.DecimalField(
        max_digits=20,
        decimal_places=2,
        default=0.00,
        verbose_name="Задолженность перед поставщиком",
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Поставщик"
        verbose_name_plural = "Поставщики"


class Factory(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название")
    email = models.EmailField(unique=True, verbose_name="Email")
    country = models.CharField(max_length=100, verbose_name="Страна")
    city = models.CharField(max_length=100, verbose_name="Город")
    address = models.CharField(max_length=200, verbose_name="Адрес")
    phone_number = models.CharField(max_length=30, verbose_name="Номер телефона")
    description = models.TextField(verbose_name="Описание", **NULLABLE)

    def __str__(self):
        return f"Завод {self.title} - {self.country}, {self.phone_number}"

    class Meta:
        verbose_name = "Завод"
        verbose_name_plural = "Заводы"


class Product(models.Model):
    factory = models.ForeignKey(Factory, on_delete=models.CASCADE, verbose_name="Завод")
    supplier = models.ForeignKey(
        Network, on_delete=models.CASCADE, verbose_name="Поставщик"
    )
    name = models.CharField(max_length=100, verbose_name="Название")
    model = models.CharField(max_length=100, verbose_name="Модель")
    release_date = models.DateTimeField(verbose_name="Дата выхода продукта на рынок")
    created_at = models.DateField(verbose_name="Дата создания", auto_now_add=True)

    def __str__(self):
        return f"Завод-{self.factory}\nПоставщик-{self.supplier}\n{self.name}"

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"


class Contact(models.Model):
    supplier = models.ForeignKey(
        Network, on_delete=models.CASCADE, verbose_name="Поставщик"
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, verbose_name="Продукт"
    )
    title = models.CharField(max_length=200, verbose_name="Название")
    email = models.EmailField(unique=True, verbose_name="Email")
    country = models.CharField(max_length=100, verbose_name="Страна")
    city = models.CharField(max_length=100, verbose_name="Город")
    address = models.CharField(max_length=200, verbose_name="Адрес")
    phone_number = models.CharField(max_length=30, verbose_name="Номер телефона")
    arrears = models.DecimalField(
        verbose_name="Задолженность", max_digits=10, decimal_places=2
    )

    def __str__(self):
        return f"Поставщик-{self.supplier}\nTовар-{self.product}"

    class Meta:
        verbose_name = "Индивидуальное предприятие"
        verbose_name_plural = "Индивидуальные предприятия"
