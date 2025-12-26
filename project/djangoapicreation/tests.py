from django.test import TestCase
from django.utils import timezone
from .models import Question
from urls import reverse
import datetime
def create_question(question_text, days):
    time = timezone.now() + datetime.timedelta(days = days)
    return Question.objects.create(question_text = question_text, pub_date = time)
class QuestionIndexViewTests(TestCase):
    def test_no_questions(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No Django are available.")
        self.assertQuerySetEqual(response.context['latest_question_list'],[])
    
    def test_past_question(self):
        create_question(question_text = 'Past question.',days = -30)
        response = self.client.get(reverse('index'))
        self.assertQuerySetEqual(
            response.context['latest_question_list'],
            ['<Question: past question.>']
            
        )
        
    def test_future_question(self):
        create_question(question_text = 'Future Question.',days = 30)
        response = self.client.get(reverse('index'))
        self.assertContains(response, 'No Django are available.')
        self.assertQuerySetEqual(response.context['latest_question_list'],[])
    def test_future_question_and_past_question(self):
        create_question(question_text="Past Question.", days = -30)
        create_question(question_text="future question.",days=30)
        response = self.client.get(reverse('index'))
        self.assertQuerySetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question.>']
            
        )
    def test_two_past_questions(self):
        create_question(question_text="past question 1.",days=-30)
        create_question(question_text='Past question 2.',days=20)
        response = self.client.get(reverse('index'))
        self.assertQuerySetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question 2.','<Question: past question 1.>']
        )
class QuestionDetailViewTests(TestCase):
    def text_future_question(self):
        future_question = create_question(question_text = 'Future question.', days = 5)
        url = reverse('details',args=(future_question.id,))
        request = self.client.get(url)
        self.assertEqual(request.status_code, 404)
    def test_past_question(self):
        past_question = create_question(question_text = 'Past Question.', days=-5)
        url = reverse('details', args = (past_question.id,))  
        response = self.client.get(url)
        self.assertContains(response, past_question.question_text)
        