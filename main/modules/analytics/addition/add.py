from main.models_addon.ya_market import Offer


def calculate_total_cost(orders):
    """
    Подсчитать доход
    :param orders: Заказы для подсчёта
    :return: Общий доход
    """
    total_cost = 0
    for order in orders:
        total_cost += order.total_price
    return total_cost


def calculate_total_net_cost(orders, offers):
    """
    Подсчитать себестоимость
    :param orders: Заказы для подсчёта
    :param user: ID пользователя
    :return: Общая себестоимость
    """
    total_net_cost = 0
    for order in orders:
        total_net_cost += order.total_net_price(offers)
    return total_net_cost


def calculate_revenue(income, net_cost):
    """
    Ф-ия для подсчёта выручки. Рассчитывается по простой формуле *income* - *net_cost*
    :param income: Доход
    :param net_cost: Себестоимость
    :return: Выручка
    """
    return income - net_cost


def calculate_profitability(income, revenue):
    return income / revenue * 100


class SecondaryStats:
    """
    Класс второстепенных stats.
    """

    def __init__(self, time='', orders=None, request=None):
        """
        Инициализация объекта
        :param time: В какое время подсчитывалось время(прошлый, текущий месяц и т.п.). Строка должна отвечать на вопрос
                     **когда?**
        :param orders: Заказы
        """
        if orders is not None:
            self.time = time
            self.amount = len(orders)
            self.total_cost = calculate_total_cost(orders)
            if request:
                self.total_net_cost = calculate_total_net_cost(orders, offers=Offer.objects.filter(user=request.user))
            else:
                self.total_net_cost = 0
            self.revenue = calculate_revenue(float(self.total_cost), float(self.total_net_cost))


class Stat:
    """
    Класс параметра для статистики.
    """
    def __init__(self, name=None, all_orders=None,
                 included_statuses=('DELIVERY', 'DELIVERED', 'PARTIALLY_RETURNED', 'PICKUP', 'PROCESSING'),
                 request=None):
        """
        Инициализация объекта класса параметр
        :param name: Название параметра
        :param all_orders: Заказы, лист из 2 объектов - заказы за пред. месяц и за тек. месяц соответственно
        :param included_statuses: Какие статусы для фильтра должны быть, если не заданы то берутся стандартные:
            'DELIVERY', 'DELIVERED', 'PARTIALLY_RETURNED', 'PICKUP', 'PROCESSING'
        """
        if len(all_orders) == 1:
            all_orders.append(None)
        filtered_orders = []
        for in_orders in all_orders:
            if in_orders is not None:
                filtered_orders.append(in_orders.filter(status__in=included_statuses))
            else:
                filtered_orders.append(None)

        self.secondary_stats = [
            SecondaryStats('в этом месяце', filtered_orders[0], request=request),
            SecondaryStats('ранее', filtered_orders[1], request=request)
        ]
        self.name = name
