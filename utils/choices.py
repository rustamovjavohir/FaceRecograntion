from django.db.models import TextChoices


class UserRoleChoices(TextChoices):
    ADMIN = "admin", "Администратор"
    SUPER_ADMIN = "super_admin", "Супер администратор"
    SHOP_ASSISTANT = "shop_assistant", "Продавец"
    RISK_MANAGER = "risk_manager", "Риск менеджер"
    SCORING_MANAGER = "scoring_manager", "Скоринг менеджер"
    OPERATOR = "operator", "Оператор"
    PARTNER = "partner", "Партнер"
    ANALYST = "analyst", "Аналитик"
    RETAIL_OPERATOR = "retail_operator", "Оператор розницы"
    USER = "user", "Пользователь"
    MANAGER = "manager", "Менеджер"
    CONTENT_MANAGER = "content_manager", "Контент менеджер"
    SPECTATOR = "spectator", "Наблюдатель"
    DIRECTOR = "director", "Директор"
    SUPER_MANAGER = "super_manager", "Супер менеджер"
    SUPER_OPERATOR = "super_operator", "Супер оператор"
    ACCOUNTING = "accounting", "Бухгалтерия"
    DISPATCHER = "dispatcher", "Диспетчер"
    DRIVER = "driver", "Водитель"
    CLIENT = "client", "Клиент"


class AuthStatusChoices(TextChoices):
    NEW = "new", "Новый"
    PHONE_VERIFY = "phone_verify", "Телефон подтвержден"
    HALF_DONE = "half_done", "Частично заполнен"
    VERIFY = "verify", "На проверке"
    DONE = "done", "Заполнен"


class ClientType(TextChoices):
    CRM = "crm", "CRM"
    SITE = "site", "Сайт"
    TELEGRAM = "telegram", "Телеграм"
    _1C = "1c", "1C"


class PaymentTypeChoices(TextChoices):
    CASH = "cash", "Наличные"
    CARD = "card", "Карта"
    NON_CASH = "non_cash", "Безналичный расчет"
    BONUS = "bonus", "Бонусы"


class ShopTypeChoices(TextChoices):
    SHOP = "shop", "Магазин"
    WAREHOUSE = "warehouse", "Склад"
    SERVICE = "service", "Сервис"


class OrderTypeChoices(TextChoices):
    PURCHASE = "purchase", "Покупка"
    INSTALLMENT = "installment", "Рассрочка"


class ShippingTypeChoices(TextChoices):
    PICKUP = "pickup", "Самовывоз"
    DELIVERY = "delivery", "Доставка"


class LanguageChoices(TextChoices):
    RU = "ru", "Русский"
    UZ = "uz", "O'zbekcha"
    EN = "en", "English"


class GenderChoices(TextChoices):
    MALE = "male", "Мужчина"
    FEMALE = "female", "Женщина"


class KATMGenderChoices(TextChoices):
    MALE = "1", "Мужчина"
    FEMALE = "2", "Женщина"


class CurrencyChoices(TextChoices):
    USD = "USD", "Доллар"
    EUR = "EUR", "Евро"
    RUB = "RUB", "Рубль"
    UZS = "UZS", "Сум"


class OrderStatusChoices(TextChoices):
    NEW = "new", "Новый"
    ACCEPTED = "accepted", "Принят"
    IN_PROGRESS = "in_progress", "В процессе"
    DONE = "done", "Выполнен"
    CANCELED = "canceled", "Отменен"


class OrderInstallmentStatusChoices(TextChoices):
    WAITING = "waiting", "Ожидает"
    ON_TIME = "on_time", "Вовремя"
    DELAYED = "delayed", "Задержка"
    PAID = "paid", "Оплачен"
    EXPIRED = "expired", "Просрочен"


class RegionChoices(TextChoices):
    TASHKENT = "tashkent", "Ташкент"
    TASHKENT_REGION = "tashkent-region", "Ташкентская область"
    ANDIJAN = "andijan", "Андижан"
    BUKHARA = "bukhara", "Бухара"
    JIZZAKH = "jizzakh", "Джизак"
    KASHKADARYA = "kashkadarya", "Кашкадарья"
    NAMANGAN = "namangan", "Наманган"
    NAVOIY = "navoiy", "Навоий"
    SAMARQAND = "samarqand", "Самарканд"
    SURKHANDARYA = "surkhandarya", "Сурхандарья"
    SIRDARYA = "sirdarya", "Сырдарья"
    FERGANA = "ferghana", "Фергана"
    KHOREZM = "khorezm", "Хорезм"
    KARAKALPAKSTAN = "karakalpakstan", "Каракалпакстан"


class ApplicationStatusChoices(TextChoices):
    NEW = "new", "Новый"
    CHECKING = "checking", "Проверка"
    COMPLETED = "completed", "Завершенный"
    USED = "used", "Использованный"
    EXPIRED = "expired", "Просроченный"


class OperatorAnswerChoices(TextChoices):
    IN_PROGRESS = "in_progress", "В обработке"
    DID_NOT_ANSWER_THE_CALL = "did_not_answer_the_call", "Не ответила(а) на звонки"
    REJECTED = "rejected", "Отклонен"
    SOLD = "sold", "Продан"
    REPEAT_ORDER = "repeat_order", "Повторный заказ"


class ApplicationAnswerChoices(TextChoices):
    ACCEPTED = "accepted", "Принят"
    REJECTED = "rejected", "Отклонен"
    INCORRECT = "incorrect", "Плохая заявка"


class DocTypeChoices(TextChoices):
    PASSPORT = "6", "Паспорт"
    ID_CARD = "0", "ID карта"


class LiveStatusChoices(TextChoices):
    DEAD = "0", "Мертвый"
    LIVE = "1", "Живой"


class CardPlumStatusChoices(TextChoices):
    ACTIVE = "0", "Активный"
    CONFIRMATION_LIMIT_EXCEEDED = "1", "Превышен лимит ввода кода подтверждения"
    BLOCKED_PIN = "2", "Заблокировано из-за неправильного ввода PIN-кода"
    TEMPORARY_BLOCKED_BY_CLIENT = "3", "Временно заблокировано клиентом"
    BLOCKED_IN_PC = "4", "Заблокировано в ПЦ"
    FAILED_UPDATE_DATA = "5", "Не удалось обновить данные"
    CARD_EXPIRED = "6", "Карта просрочена"
    INACTIVE = "7", "Неактивный"
    BLOCKED_BY_MYUZCARD = "8", "Заблокировано MY UzCard"
    SMS_INFO_INACTIVE = "9", "SMS-информирование неактивно"
    REISSUED = "10", "Перевыпущен"


class KATMReportChoices(TextChoices):
    START = "123", "START"
    INPS = "125", "ЗАРАБОТНАЯ ПЛАТА ПО ИНПС"


class FileReportChoices(TextChoices):
    MIB = "mib", "MIB"
    CRIF = "crif", "CRIF"


class CardTypeChoices(TextChoices):
    VISA = "visa", "Visa"
    MASTERCARD = "mastercard", "MasterCard"
    HUMO = "humo", "Humo"
    UZCARD = "uzcard", "UzCard"
    OTHER = "other", "Другой"


class PaymentStatusChoices(TextChoices):
    DONE = 'done', 'Оплачен'
    CANCELED = 'canceled', 'Отменен'


class Contact1cStatusChoices(TextChoices):
    WAIT = 'wait', 'В ожидании'
    SUCCESS = 'success', 'Успех'
    UNSUCCESS = 'unsuccess', 'Неудачный'


class FeedbackStatusChoices(TextChoices):
    NEW = 'new', '🆕Новый'
    PENDING_ANSWER = 'pending_answer', '🕐Ожидает ответа'
    ANSWERED = 'answered', '✅Отвечен'
    COMPLETED = 'completed', 'Завершен'


class PlumCardTypeChoices(TextChoices):
    HUMO = "1", "Humo"
    UZCARD = "0", "UzCard"


class BalanceActionChoices(TextChoices):
    ADD = "add", "Пополнение"
    SUBTRACT = "subtract", "Списание"
    CHANGE = "change", "Изменение"


class BalanceSourceChoices(TextChoices):
    CRM = "crm", "CRM"
    V_1C = "1c", "1C"
    CASHBACK = "cashback", "Кэшбэк"
    PROMO = "promo", "Промокод"


class DeliveryOrderStatusChoices(TextChoices):
    NEW = "new", "Новый"
    COURIER_APPOINTED = "appointed", "Курьер назначен"
    COURIER_ACCEPTED_ORDER = "accepted", "Курьер принял заказ"
    COURIER_LOCATION_A = "location_a", "Курьер  в пункте А"
    LOADING = "loading", "Загружает"
    DELIVERED = "delivered", "Доставляется"
    COURIER_LOCATION_B = "location_b", "Курьер  в пункте Б"
    SHIPPING = "shipping", "Отгружает"
    DONE = "done", "Заказ завершен"
    CANCELED = "canceled", "Отменен"


class DeliveryDriverTypeChoices(TextChoices):
    CAR = "car", "Автомобиль"
    TRUCK = "truck", "Грузовик"
