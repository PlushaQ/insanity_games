from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponseRedirect
from django.core.mail import send_mail

from games.models import Game
from .models import News

# Create your views here.


def homepage(request):
    games = Game.objects.all
    news = News.objects.latest('publish_date')
    return render(request, 'homepage.html', {'games': games, 'news': news})


def about_us(request):
    history = "Our company was founded in 2022 by M. Fularz, K. Gasimov, P. Czerwiński, R. Piszczek."
    mission = """Our mission is to create innovative and engaging games that push the boundaries of entertainment.
    We strive to inspire and excite players around the world with immersive gameplay experiences that spark their imagination and leave them wanting more.
    Our team is dedicated to the craft of game development, constantly learning and evolving to create games that stand out in an ever-changing industry.
    We are committed to fostering a culture of creativity, collaboration, and inclusion, where every team member can contribute their unique talents and ideas.
    At our core, we are passionate about games and the impact they can have on people's lives.
    And we will continue to push ourselves to create games that inspire, challenge, and entertain."""
    values = [
    "Creativity: We believe in fostering a culture of creativity, where every team member is encouraged to explore new ideas and push the boundaries of game development.",
    "Innovation: We strive to be at the forefront of innovation in the gaming industry, constantly seeking new ways to create unique and engaging gameplay experiences for our players.",
    "Quality: We are committed to delivering high-quality games that meet and exceed the expectations of our players, paying close attention to every detail of the development process.",
    "Collaboration: We believe in the power of collaboration and teamwork, working closely with each other and our partners to create the best possible games.",
    "Diversity and Inclusion: We are committed to fostering a diverse and inclusive workplace, where every team member feels valued and empowered to contribute their unique talents and perspectives.",
    "Player-Centric: We prioritize the needs and desires of our players, always striving to create games that are fun, engaging, and enjoyable for everyone.",
    "Learning and Growth: We believe in the importance of continual learning and growth, both as individuals and as a team, and strive to provide opportunities for our team members to develop their skills and reach their full potential. "
    ]
    return render(request, 'about_us.html', {'history': history, 'mission': mission, 'values': values })


def contact_us(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        message = request.POST.get('message', '')
        print("\n", settings.EMAIL_HOST_PASSWORD, "\n")
        send_mail('Contact Form',
                  'Name: {}\nEmail: {}\nMessage: {}'.format(name, email, message),
                  settings.DEFAULT_FROM_EMAIL,
                  [settings.DEFAULT_FROM_EMAIL],
                  fail_silently=False)

        # redirect to a thank-you page
        return HttpResponseRedirect('thanks/')

    return render(request, 'contact_us.html', {})


def thanks(request):
    return render(request, 'thanks.html')


def all_news(request):
    news = News.objects.all
    return render(request, 'news.html', {'all_news': news})
