from rest_framework.views import APIView
from apps.inventories.models import Inventory
from apps.inventories.serializer import InventorySerializer
from rest_framework.response import Response
from rest_framework import status


class InventoryList(APIView):
    def get(self, request):
        inventories = Inventory.objects.all()  # Complex Data
        serializer = InventorySerializer(inventories, many=True)
        return Response(serializer.data)



class InventoryCreate(APIView):
    def post(self, request):
        serializer = InventorySerializer(data=request.data)
        if serializer.is_valid():
            print(serializer)
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class InventoryDeleteRequest(APIView):
    def delete_inventory_by_pk(self, pk):
        try:
            Inventory.objects.filter(id=pk).delete()
        except:
            return Response({
                'error': 'Inventory does not exist'
            }, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        deletionArray = request.data
        response = {}
        for element in deletionArray:
            if(Inventory.objects.filter(id=element)):
                self.delete_inventory_by_pk(pk=element)
                response['id:'+str(element) +
                         '_report'] = 'error: inventory deleted successfully'
            else:
                response['id:'+str(
                    element)+'_report'] = 'error: the inventory could not be deleted, please check if the id is correct'
        return Response(response)


class InventorySoftDelete(APIView):
    def delete_inventory_by_pk(self, pk):
        try:
            Inventory.objects.filter(id=pk).bulk_update()
        except:
            return Response({
                'error': 'Inventory does not exist'
            }, status=status.HTTP_404_NOT_FOUND)
            # TODO ADD BULK UPDATE TO SOFTDELETE ITEMS ON TABLE

    def post(self, request):
        deletionArray = request.data
        response = {}
        for element in deletionArray:
            if(Inventory.objects.filter(id=element)):
                self.delete_inventory_by_pk(pk=element)
                response['id:'+str(element) +
                         '_report'] = 'error: inventory deleted successfully'
            else:
                response['id:'+str(
                    element)+'_report'] = 'error: the inventory could not be deleted, please check if the id is correct'
        return Response(response)


class InventoryDetail(APIView):
    def get_inventory_by_pk(self, pk):
        try:
            inventory = Inventory.objects.get(pk=pk)
        except:
            return Response({
                'error': 'Inventory does not exist'
            }, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        inventory = self.get_inventory_by_pk(pk)
        serializer = InventorySerializer(inventory)
        return Response(serializer.data)

    def put(self, request, pk):
        inventory = Inventory.objects.get(pk=pk)
        if request.method == 'PUT':
            serializer = InventorySerializer(inventory, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
