from rest_framework import viewsets
from .serializers import PictureSerializer
from .filters import PictureFilter
from .models import Pictures
from colormap import rgb2hex
from PIL import Image


class PictureViewset(viewsets.ModelViewSet):
    serializer_class = PictureSerializer
    filterset_class = PictureFilter
    queryset = Pictures.objects.all()


    def perform_create(self, serializer,):
        
        form_data = self.request.data
        img_data = form_data['image']
        img = Image.open(img_data)
        img = img.quantize(colors=3, kmeans=2).convert('RGB')
        w, h = img.size
        dom_colors = sorted(img.getcolors(2 ** 24), reverse=True)[:1]
        hex_dom = rgb2hex(0, 128, 64)

        serializer.save(
            width=w,
            height=h,
            dominant_hex=hex_dom
        )