from rest_framework.views import APIView
from apps.orders.models import Order
from apps.orders.serializer import OrderSerializer
from rest_framework.response import Response
from rest_framework import status


class OrderList(APIView):
    def get(self, request):
        orders = Order.objects.all()  # Complex Data
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)


class OrderCreate(APIView):
    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            print(serializer)
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class OrderDeleteRequest(APIView):
    def delete_order_by_pk(self, pk):
        try:
            Order.objects.filter(id=pk).delete()
        except:
            return Response({
                'error': 'Order does not exist'
            }, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        deletionArray = request.data
        response = {}
        for element in deletionArray:
            if(Order.objects.filter(id=element)):
                self.delete_order_by_pk(pk=element)
                response['id:'+str(element) +
                         '_report'] = 'error: order deleted successfully'
            else:
                response['id:'+str(
                    element)+'_report'] = 'error: the order could not be deleted, please check if the id is correct'
        return Response(response)


class OrderSoftDelete(APIView):
    def delete_order_by_pk(self, pk):
        try:
            Order.objects.filter(id=pk).bulk_update()
        except:
            return Response({
                'error': 'Order does not exist'
            }, status=status.HTTP_404_NOT_FOUND)
            # TODO ADD BULK UPDATE TO SOFTDELETE ITEMS ON TABLE

    def post(self, request):
        deletionArray = request.data
        response = {}
        for element in deletionArray:
            if(Order.objects.filter(id=element)):
                self.delete_order_by_pk(pk=element)
                response['id:'+str(element) +
                         '_report'] = 'error: order deleted successfully'
            else:
                response['id:'+str(
                    element)+'_report'] = 'error: the order could not be deleted, please check if the id is correct'
        return Response(response)


class OrderDetail(APIView):
    def get_order_by_pk(self, pk):
        try:
            order = Order.objects.get(pk=pk)
        except:
            return Response({
                'error': 'Order does not exist'
            }, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        order = self.get_order_by_pk(pk)
        serializer = OrderSerializer(order)
        return Response(serializer.data)

    def put(self, request, pk):
        order = Order.objects.get(pk=pk)
        if request.method == 'PUT':
            serializer = OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
