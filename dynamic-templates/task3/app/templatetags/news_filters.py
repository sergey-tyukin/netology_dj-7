from datetime import datetime, timedelta
from django import template


register = template.Library()


@register.filter
def format_date(value):
    def get_hours(hours):
        return {
            hours == 0 or 5 <= hours <= 20: 'часов',
            hours == 1 or hours == 21: 'час',
            2 <= hours <= 4 or 22 <= hours <= 24: 'часа'
        }[True]

    post_time = datetime.fromtimestamp(value)
    current_time = datetime.now()
    if current_time - post_time <= timedelta(minutes=10):
        return "Только что"
    if current_time - post_time <= timedelta(hours=24):
        hours = (current_time - post_time).seconds // 3600
        return f"{hours} {get_hours(hours)} назад"
    return post_time.strftime("%Y-%m-%d")


@register.filter
def format_score(value):
    return {
        value < -5: 'всё пропало',
        -5 <= value <= 5: 'норм',
        value > 5: 'отлично'
    }[True]


@register.filter
def format_num_comments(value):
    return {
        value == 0: 'Оставьте комментарий',
        1 <= value <= 50: f'{value} комментариев',
        value > 50: '50+'
    }[True]


@register.filter
def format_selftext(value, count=5):
    text_list = value.split()
    return ' '.join(text_list[:count]) + ' ... ' + ' '.join(text_list[-count:])
