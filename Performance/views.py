from django.shortcuts import render, redirect
from .models import Semester, Subject
from .forms import SemesterForm, SubjectForm

def manage_performance(request):
    semesters = Semester.objects.filter(user=request.user)
    semester_form = SemesterForm()
    subject_form = SubjectForm()

    if request.method == "POST":
        if 'add_semester' in request.POST:
            semester_form = SemesterForm(request.POST)
            if semester_form.is_valid():
                semester = semester_form.save(commit=False)
                semester.user = request.user
                semester.save()
                return redirect('manage_performance')

        elif 'add_subject' in request.POST:
            subject_form = SubjectForm(request.POST)
            if subject_form.is_valid():
                subject = subject_form.save(commit=False)
                subject.semester_id = request.POST.get('semester_id')  # Assign semester ID dynamically
                subject.save()
                return redirect('manage_performance')

    return render(request, 'performance/manage_performance.html', {
        'semesters': semesters,
        'semester_form': semester_form,
        'subject_form': subject_form,
    })

