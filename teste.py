# def get_queryset(self):
#     return Promovare.objects.filter(metoda_de_promovare='TL')
#
#
# def get_context_data(self, **kwargs):
#     context = super().get_context_data(**kwargs)
#     context['searches'] = Search.objects.all()
#     context['promovares'] = Promovare.objects.all()
#     context['4_tl'] = Anunt.objects.filter(promovare__metoda_de_promovare='TL').order_by('-pret')[:4]
#     return context
