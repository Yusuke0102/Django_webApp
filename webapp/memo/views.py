from django.shortcuts import render, redirect, get_object_or_404
from .models import Memo
from .forms import MemoForm

def memo_home(request):
    memos = Memo.objects.order_by("-updated_at")
    return render(request, "memo/memo_list.html", {"memos": memos})

def memo_create(request):
    if request.method == "POST":
        form = MemoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("memo_home")
    else:
        form = MemoForm()
    return render(request, "memo/memo_form.html", {"form": form, "mode": "create"})
class Variable:
    cnt = 0
C = Variable()

def hoge_main(request):
    if C.cnt == 10 or C.cnt == -10:
        hoge_init()
        return render(request, "memo/hoge.html", {"count": C.cnt, "Res": "I_Limit"})

    if request.GET.get("hoge") == "Init":
        hoge_init()
        return render(request, "memo/hoge.html", {"count": C.cnt, "Res": "I_Init"})
    elif request.method == "GET":
        C.cnt = hoge_GET()
    elif request.method == "POST":
        C.cnt = hoge_POST()
    Res = C.cnt%2
    return render(request, "memo/hoge.html", {"count": C.cnt, "Res": Res})

def hoge_init():
    C.cnt = 0 

def hoge_GET():
    C.cnt = C.cnt + 1
    return C.cnt

def hoge_POST():
    C.cnt = C.cnt - 1
    return C.cnt 

#Test function
def memo_create2(request):
    if request.method == "GET":
        test = "Hello. Django!"
        return render(request, "memo/memo_form.html", {"hoge": test, "mode2": "hogehoge"})
    elif request.method == "POST":  
        test = "This is POST method."
        return render(request, "memo/memo_form.html", {"hoge": test, "mode2": "hogehoge"})

def memo_update(request, pk):
    memo = get_object_or_404(Memo, pk=pk)
    if request.method == "POST":
        form = MemoForm(request.POST, instance=memo)
        if form.is_valid():
            form.save()
            return redirect("memo_home")
    else:
        form = MemoForm(instance=memo)
    return render(request, "memo/memo_form.html", {"form": form, "mode": "update", "memo": memo})

def memo_delete(request, pk):
    memo = get_object_or_404(Memo, pk=pk)
    if request.method == "POST":
        memo.delete()
        return redirect("memo_home")
    return render(request, "memo/memo_confirm_delete.html", {"memo": memo})
