# Generated by Django 3.1.6 on 2021-02-11 09:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Barcode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('barcode', models.CharField(max_length=255, verbose_name='Штрихкод товара')),
            ],
        ),
        migrations.CreateModel(
            name='CustomsCommodityCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(help_text='Формат кода: 10 цифр без пробелов', max_length=10, verbose_name='Код товара в единой Товарной номенклатуре внешнеэкономической деятельности (ТН ВЭД)')),
            ],
        ),
        migrations.CreateModel(
            name='ManufacturerCountry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Страна производства товара')),
            ],
        ),
        migrations.CreateModel(
            name='Mapping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('market_sku', models.IntegerField(verbose_name='SKU на Яндексе — идентификатор текущей карточки товара на Маркете')),
                ('model_id', models.IntegerField(help_text='Например, две лопатки разных цветов имеют разные SKU на Яндексе (параметр market_sku), но одинаковый идентификатор модели товара', verbose_name='Идентификатор модели для текущей карточки товара на Маркете')),
                ('category_id', models.IntegerField(verbose_name='Идентификатор категории для текущей карточки товара на Маркете')),
                ('mapping_type', models.CharField(choices=[('BASE', 'Информация о текущей карточке товара на Маркете'), ('AWAITING_MODERATION', 'Информация о карточке товара на Маркете, проходящей модерацию для данного товара'), ('REJECTED', 'Информация о последней карточке товара на Маркете, отклоненной на модерации для данного товара')], max_length=19, verbose_name='Тип маппинга')),
            ],
        ),
        migrations.CreateModel(
            name='ProcessingStateNote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note_type', models.CharField(choices=[('ASSORTMENT', 'товар производится в разных вариантах. Каждый из них нужно описать как отдельный товар'), ('CANCELLED', 'товар отозван с модерации по вашей инициативе'), ('CONFLICTING_INFORMATION', 'вы предоставили потиворечивую информацию о товаре. Параметры, которые нужно исправить, указаны в параметре payload'), ('DEPARTMENT_FROZEN', 'правила размещения товаров в данной категории перерабатываются, поэтому товар пока не может пройти модерацию'), ('INCORRECT_INFORMATION', 'информация о товаре, которую вы предоставили, противоречит описанию от производителя. Параметры, которые нужно исправить, указаны в параметре payload'), ('LEGAL_CONFLICT', 'товар не прошел модерацию по юридическим причинам. Например, он официально не продается в России или у вас нет разрешения на его продажу'), ('NEED_CLASSIFICATION_INFORMATION', 'информации о товаре, которую вы предоставили, не хватает, чтобы отнести его к категории. Проверьте, что правильно указали название, категорию, производителя и страны производства товара, а также URL изображений или страниц с описанием, по которым можно идентифицировать товар'), ('NEED_INFORMATION', 'товар раньше не продавался в России и пока не размещается на Маркете. Для него можно создать карточку'), ('NEED_PICTURES', 'для идентификации товара нужны его изображения'), ('NEED_VENDOR', 'неверно указан производитель товара'), ('NO_CATEGORY', 'товары из указанной категории пока не размещаются на Маркете. Если категория появится, товар будет снова отправлен на модерацию'), ('NO_KNOWLEDGE', 'товары из указанной категории пока не размещаются на Маркете. Если категория появится, товар будет снова отправлен на модерацию'), ('NO_PARAMETERS_IN_SHOP_TITLE', 'товар производится в разных вариантах, и из указанного названия непонятно, о каком идет речь. Параметры, которые нужно добавить в название товара, указаны в параметре payload'), ('NO_SIZE_MEASURE', 'для этого товара нужна размерная сетка. Отправьте ее в службу поддержки или вашему менеджеру. Требования к размерной сетке указаны в параметре payload'), ('UNKNOWN', 'товар не прошел модерацию по другой причине. Обратитесь в службу поддержки или к вашему менеджеру')], max_length=31, verbose_name='Тип причины, по которой товар не прошел модерацию')),
                ('payload', models.CharField(help_text='Возвращается, если параметр type имеет одно из следующих значений: CONFLICTING_INFORMATION, INCORRECT_INFORMATION, NO_PARAMETERS_IN_SHOP_TITLE, NO_SIZE_MEASURE.', max_length=2000, verbose_name='Дополнительная информация о причине отклонения товара')),
            ],
        ),
        migrations.CreateModel(
            name='Timing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_period', models.BigIntegerField(verbose_name='Срок годности в единицах, указанных в параметре time_unit')),
                ('time_unit', models.CharField(choices=[('HOUR', 'часы'), ('DAY', 'дни'), ('WEEK', 'недели'), ('MONTH', 'месяцы'), ('YEAR', 'годы')], max_length=5, verbose_name='Единица измерения срока годности')),
                ('comment', models.CharField(help_text='Например: Хранить в сухом помещении', max_length=2000, verbose_name='Дополнительные условия использования в течение срока годности')),
                ('timing_type', models.IntegerField(choices=[(0, 'shelf_life'), (1, 'life_time'), (2, 'guarantee_period')], help_text='Определяет, где в каком свойстве модели будет находиться свойство', verbose_name='Тип таймингового поля')),
            ],
        ),
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=2000, verbose_name='URL изображения или страницы с описанием товара')),
            ],
        ),
        migrations.CreateModel(
            name='WeightDimension',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('length', models.FloatField(help_text='Значение с точностью до тысячных, разделитель целой и дробной части — точка. Пример: 65.55', verbose_name='Длина упаковки в сантиметрах')),
                ('width', models.FloatField(help_text='Значение с точностью до тысячных, разделитель целой и дробной части — точка. Пример: 50.7', verbose_name='Ширина упаковки в сантиметрах')),
                ('height', models.FloatField(help_text='Значение с точностью до тысячных, разделитель целой и дробной части — точка. Пример: 20.0', verbose_name='Высота упаковки в сантиметрах')),
                ('weight', models.FloatField(help_text='С учетом упаковки (брутто). Значение с точностью до тысячных, разделитель целой и дробной части — точка. Пример: 1.001', verbose_name='Вес товара в килограммах')),
            ],
        ),
        migrations.CreateModel(
            name='ProcessingState',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('READY', 'товар прошел модерацию. Чтобы разместить его на Маркете, установите для него цену и создайте поставку на склад. Подробнее см. в разделе Загрузка каталога товаров, а также в разделе "Как поставить товары на склад" Справки Маркета для моделей FBY, FBY+ и FBS'), ('IN_WORK', 'товар проходит модерацию. Это занимает несколько дней'), ('NEED_CONTENT', 'для товара без SKU на Яндексе market_sku нужно найти карточку самостоятельно (через API или личный кабинет магазина) или создать ее, если товар еще не продается на Маркете'), ('NEED_INFO', 'товар не прошел модерацию из-за ошибок или недостающих сведений в описании товара. Информация о причинах отклонения возвращается в параметре notes'), ('REJECTED', 'товар не прошел модерацию, так как Маркет не планирует размещать подобные товары'), ('SUSPENDED', 'товар не прошел модерацию, так как Маркет пока не размещает подобные товары'), ('OTHER', 'товар не прошел модерацию по другой причине. Обратитесь в службу поддержки или к вашему менеджеру')], max_length=12, verbose_name='Статус публикации товара')),
                ('notes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.processingstatenote', verbose_name='Причины, по которым товар не прошел модерацию')),
            ],
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop_sku', models.CharField(max_length=255, verbose_name='SKU товара в нашем магазине')),
                ('name', models.CharField(max_length=255, verbose_name='Название товара')),
                ('category', models.CharField(max_length=255, verbose_name='Категория товара')),
                ('manufacturer', models.CharField(help_text='Компания, которая произвела товар, ее адрес и регистрационный номер (если есть)', max_length=255, verbose_name='Изготовитель товара')),
                ('vendor', models.CharField(max_length=255, verbose_name='Бренд товара')),
                ('vendor_code', models.CharField(max_length=255, verbose_name='Артикул товара от производителя')),
                ('description', models.CharField(max_length=2000, verbose_name='Описание товара')),
                ('certificate', models.CharField(help_text='Документ по его номеру можно найти в личном кабинете магазина', max_length=255, verbose_name='Номер документа на товар')),
                ('availability', models.CharField(choices=[('ACTIVE', 'поставки будут'), ('INACTIVE', 'поставок не будет: товар есть на складе, но вы больше не планируете его поставлять. Через 60 дней после того, как товар закончится на складе, этот статус изменится на DELISTED'), ('DELISTED', 'архив: товар закончился на складе, и его поставок больше не будет. Если товар вернется на склад (например, покупатель вернет заказ), этот статус изменится на INACTIVE.')], max_length=8, verbose_name='Планы по поставкам')),
                ('transport_unit_size', models.IntegerField(help_text='Например, если вы поставляете детское питание коробками по 6 баночек, значение равно 6', verbose_name='Количество единиц товара в одной упаковке, которую вы поставляете на склад')),
                ('min_shipment', models.IntegerField(help_text='Например, если вы поставляете детское питание партиями минимум по 10 коробок, а в каждой коробке по 6 баночек, значение равно 60', verbose_name='Минимальное количество единиц товара, которое вы поставляете на склад')),
                ('quantum_of_supply', models.IntegerField(help_text='Например, если вы поставляете детское питание партиями минимум по 10 коробок и хотите добавлять к минимальной партии по 2 коробки, а в каждой коробке по 6 баночек, значение равно 12.', verbose_name='Добавочная партия: по сколько единиц товара можно добавлять к минимальному количеству min_shipment')),
                ('supply_schedule_days', models.CharField(choices=[('MONDAY', 'понедельник'), ('TUESDAY', 'вторник'), ('WEDNESDAY', 'среда'), ('THURSDAY', 'четверг'), ('FRIDAY', 'пятница'), ('SATURDAY', 'суббота'), ('SUNDAY', 'воскресенье')], max_length=9, verbose_name='День недели, в который вы поставляете товары на склад')),
                ('delivery_duration_days', models.IntegerField(verbose_name='Срок, за который вы поставляете товары на склад, в днях')),
                ('box_count', models.IntegerField(default=1, help_text='Например, кондиционер занимает два места: внешний и внутренний блоки в двух коробках', verbose_name='Сколько мест (если больше одного) занимает товар')),
                ('barcodes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.barcode', verbose_name='Штрихкоды товара')),
                ('customs_commodity_codes', models.ForeignKey(help_text='Список кодов товара в единой Товарной номенклатуре внешнеэкономической деятельности (ТН ВЭД), если товар подлежит особому учету (например, в системе "Меркурий" как продукция животного происхождения или в системе "Честный ЗНАК"). Может содержать только один вложенный код ТН ВЭД.', on_delete=django.db.models.deletion.CASCADE, to='main.customscommoditycode', verbose_name='Список кодов товара в единой ТН ВЭД')),
                ('manufacturer_countries', models.ManyToManyField(help_text='Содержит от одной до 5 стран', to='main.ManufacturerCountry', verbose_name='Список стран, в которых произведен товар')),
                ('mappings', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.mapping', verbose_name='Привязки карточек на Я.Маркете')),
                ('processing_states', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.processingstate', verbose_name='История статусов публикации товара на Маркете')),
                ('timings', models.ForeignKey(help_text='Срок годности, срок службы, гарантийный срок', on_delete=django.db.models.deletion.CASCADE, to='main.timing', verbose_name='Тайминги товара')),
                ('urls', models.ForeignKey(help_text='страниц с описанием товара на вашем сайте; фотографий товара в хорошем качестве. Содержит хотя бы один URL', on_delete=django.db.models.deletion.CASCADE, related_name='urls', to='main.weightdimension', verbose_name='Список URL')),
                ('weight_dimensions', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='weight_dimensions', to='main.weightdimension', verbose_name='Габариты упаковки и вес товара')),
            ],
        ),
    ]
