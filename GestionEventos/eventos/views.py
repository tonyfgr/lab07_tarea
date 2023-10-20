from django.shortcuts import get_object_or_404, redirect, render
from .models import Evento, Usuario, RegistroEvento
from .forms import EventoForm, UsuarioForm, RegistroEventoForm

def crear_evento(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_eventos') 
    else:
        form = EventoForm()
    return render(request, 'crear_evento.html', {'form': form})

def crear_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_usuarios')
    else:
        form = UsuarioForm()
    return render(request, 'crear_usuario.html', {'form': form})

def crear_registro_evento(request):
    if request.method == 'POST':
        form = RegistroEventoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_registros_evento') 
    else:
        form = RegistroEventoForm()
    return render(request, 'crear_registro_evento.html', {'form': form})

def contar_usuarios_por_evento(evento_id):
    return RegistroEvento.objects.filter(evento__id=evento_id).count()

def lista_eventos(request):
    eventos = Evento.objects.order_by('evento')[:6]
    eventos_con_usuarios = []
    for evento in eventos:
        cantidad_usuarios = contar_usuarios_por_evento(evento.id)
        eventos_con_usuarios.append({'evento': evento, 'cantidad_usuarios': cantidad_usuarios})
    context = {
        'eventos': eventos, 
        'eventos_con_usuarios': eventos_con_usuarios 
    }
    return render(request, 'lista_eventos.html', context)

def detalle_evento(request, evento_id):
    evento = Evento.objects.get(id=evento_id)
    registros = RegistroEvento.objects.filter(evento=evento)
    return render(request, 'detalle_evento.html', {'evento': evento, 'registros': registros})

def lista_usuarios(request):
    # Obtén la lista de usuarios desde la base de datos
    usuarios = Usuario.objects.all()

    # Renderiza el template para la lista de usuarios y pasa los datos
    return render(request, 'lista_usuarios.html', {'usuarios': usuarios})

def lista_registros_evento(request):
    # Obtén la lista de registros de eventos desde la base de datos
    registros_evento = RegistroEvento.objects.all()

    # Renderiza el template para la lista de registros de eventos y pasa los datos
    return render(request, 'lista_registros_evento.html', {'registros_evento': registros_evento})

def editar_evento(request, evento_id):
    evento = get_object_or_404(Evento, pk=evento_id)
    if request.method == 'POST':
        form = EventoForm(request.POST, instance=evento)
        if form.is_valid():
            form.save()
            return redirect('lista_eventos')
    else:
        form = EventoForm(instance=evento)
    return render(request, 'editar_evento.html', {'form': form, 'evento': evento})

def editar_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, pk=usuario_id)
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('lista_usuarios')
    else:
        form = UsuarioForm(instance=usuario)
    return render(request, 'editar_usuario.html', {'form': form, 'usuario': usuario})

def editar_registro_evento(request, registro_id):
    registro = get_object_or_404(RegistroEvento, pk=registro_id)
    if request.method == 'POST':
        form = RegistroEventoForm(request.POST, instance=registro)
        if form.is_valid():
            form.save()
            return redirect('lista_registros_evento')
    else:
        form = RegistroEventoForm(instance=registro)
    return render(request, 'editar_registro_evento.html', {'form': form, 'registro': registro})

def eliminar_evento(request, evento_id):
    evento = get_object_or_404(Evento, pk=evento_id)
    evento.delete()
    return redirect('lista_eventos')

def eliminar_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, pk=usuario_id)
    usuario.delete()
    return redirect('lista_usuarios')

def eliminar_registro_evento(request, registro_id):
    registro = get_object_or_404(RegistroEvento, pk=registro_id)
    registro.delete()
    return redirect('lista_registros_evento')

