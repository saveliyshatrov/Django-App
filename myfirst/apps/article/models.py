from django.db import models

class Article(models.Model):
    article_title = models.CharField('название статьи', max_length = 200)
    article_text = models.TextField('текст статьи')
    pub_date = models.DateTimeField('дата публикации')
    
class Comment(models.Model):

	article = models.ForeignKey(Article, on_delete = models.CASCADE)
	author_name = models.CharField('имя автора', max_length = 200)
	comment_text = models.CharField('текст комментария', max_length = 200)

	def split(self, string):
		return string.split(',')

class Student(models.Model):
	student_name = models.TextField('Полное имя студента')
	student_course = models.CharField('Курс студента', max_length = 20)
	delete = models.CharField('Remove', max_length = 10)