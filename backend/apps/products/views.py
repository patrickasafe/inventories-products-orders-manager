from rest_framework.views import APIView
from apps.products.models import Product
from apps.products.serializer import ProductSerializer
from rest_framework.response import Response
from rest_framework import status


class ProductList(APIView):
    def get(self, request):
        products = Product.objects.all()  # Complex Data
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        # if serializer.is_valid():


class ProductCreate(APIView):
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            print(serializer)
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class ProductDeleteRequest(APIView):
    def delete_product_by_pk(self, pk):
        try:
            Product.objects.filter(id=pk).delete()
        except:
            return Response({
                'error': 'Product does not exist'
            }, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        deletionArray = request.data
        response = {}
        for element in deletionArray:
            if(Product.objects.filter(id=element)):
                self.delete_product_by_pk(pk=element)
                response['id:'+str(element) +
                         '_report'] = 'error: product deleted successfully'
            else:
                response['id:'+str(
                    element)+'_report'] = 'error: the product could not be deleted, please check if the id is correct'
        return Response(response)


class ProductSoftDelete(APIView):
    def delete_product_by_pk(self, pk):
        try:
            Product.objects.filter(id=pk).bulk_update()
        except:
            return Response({
                'error': 'Product does not exist'
            }, status=status.HTTP_404_NOT_FOUND)
            # TODO ADD BULK UPDATE TO SOFTDELETE ITEMS ON TABLE

    def post(self, request):
        deletionArray = request.data
        response = {}
        for element in deletionArray:
            if(Product.objects.filter(id=element)):
                self.delete_product_by_pk(pk=element)
                response['id:'+str(element) +
                         '_report'] = 'error: product deleted successfully'
            else:
                response['id:'+str(
                    element)+'_report'] = 'error: the product could not be deleted, please check if the id is correct'
        return Response(response)


class ProductDetail(APIView):
    def get_product_by_pk(self, pk):
        try:
            product = Product.objects.get(pk=pk)
        except:
            return Response({
                'error': 'Product does not exist'
            }, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        product = self.get_product_by_pk(pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def put(self, request, pk):
        product = Product.objects.get(pk=pk)
        if request.method == 'PUT':
            serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
