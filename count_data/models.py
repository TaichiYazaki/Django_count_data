from django.db import models

# Create your models here.
SCORE_CHOICE = (
    (1, '★1'),
    (2, '★2'),
    (3, '★3'),
    (4, '★4'),
    (5, '★5'),
)


class Book(models.Model):
    """本"""
    title = models.CharField('タイトル', max_length=255)
    price = models.IntegerField('価格')

    def __str__(self):
        return '{} - {}'.format(self.title, self.price)


class Review(models.Model):
    """評価"""
    point = models.IntegerField('評価点', choices=SCORE_CHOICE)
    target = models.ForeignKey(Book, verbose_name='評価対象の本',
                               on_delete=models.CASCADE)

    def __str__(self):
        return '{} - {}'.format(self.target.title,
                                self.get_point_display())
