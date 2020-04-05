from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length = 100)

class Restaurant(models.Model):
    category = models.ForeignKey(Category, on_delete = models.SET_DEFAULT, default=4)
    # ForeinKey 외부키를 시용하겠다는 뜻  바로 뒤에 나오는 Category를 참과겠다는 뜻
    # on_delete는 참조하는 모델이 삭제되었을때 어떻게 할것인 지 물어보는것
    # on_delete의 종류 : CASCADE 참조하는 요소가 삭제되면 이를 참조하는 다른 요소도 다 삭제
    #                   PROTECT 참조하는 요소를 삭제할때 오류를 발생
    #                   SET_NULL 참조하는 요소를 이를 삭제할때 참조하는 다른 요소를 NULL로 만듬
    #                   SET_DEAFAULT 참조하는 요소를 이를 삭제할때 참조하는 다른 요소들을 DEAFULT 값으로 설정
    # 아까 지정해둔 기본 기룹의 id값인 4를 default로 설정
    restaurant_name = models.CharField(max_length = 100)
    restaurant_link = models.CharField(max_length = 500)
    restaurant_content = models.TextField()
    restaurant_keyword = models.CharField(max_length = 50)