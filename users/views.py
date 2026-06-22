from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
from accounts.models import Profile
from main.models import Pot, Proof
import datetime

def mypage(request, id):
    if not request.user.is_authenticated:
        return redirect('accounts:login')

    if request.user.id != id:
        return redirect('main:dashboard')

    profile_user = get_object_or_404(User, pk=id)
    profile = get_object_or_404(Profile, user=profile_user)

    my_pots = Pot.objects.filter(participants=profile_user)
    
    completed_pots_count = my_pots.filter(is_completed=True).count()
    
    total_days = sum(pot.days for pot in my_pots)
    
    valid_proofs_count = Proof.objects.filter(user=profile_user, is_valid=True).count()
    achievement_rate = int((valid_proofs_count / total_days) * 100) if total_days > 0 else 0

    context = {
        'profile_user': profile_user,
        'profile': profile,
        'my_pots': my_pots,
        'completed_pots_count': completed_pots_count,
        'total_days': total_days,
        'achievement_rate': achievement_rate,
    }

    return render(request, 'users/mypage.html', context)
