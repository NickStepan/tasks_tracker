from django.core.exceptions import PermissionDenied

class IsUserOwnerMixin():
    def dispatch(self, request, *args, **kwargs):
        instance = self.get_object()
        
        if instance.creator != self.request.user:
            raise PermissionDenied("You are not User of this site")
        
        return super().dispatch(request, *args, **kwargs)