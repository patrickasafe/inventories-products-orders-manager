from rest_framework.response import Response
from rest_framework import generics, status


class CustomMultipleDestroyRequestAPIView(generics.DestroyAPIView):

    def __init__(self, *args, **kwargs):
        self.object_name = self.__class__.__name__[0:-29]
        super(CustomMultipleDestroyRequestAPIView,
              self).__init__(*args, **kwargs)

    def delete_inventory_by_pk(self, pk):
        """Receives a PK for delete request"""
        try:
            self.serializer_class.objects.filter(id=pk).delete()
        except ValueError:
            return Response({
                'error': f'{self.object_name.capitalize()} ID does not exist'
            }, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        deletion_array = request.data
        response = {}
        for element in deletion_array:
            if(self.serializer_class.objects.filter(id=element)):
                self.delete_inventory_by_pk(pk=element)
                response['id:'+str(element) +
                         '_report'] = f'The {self.object_name.capitalize()} has been deleted successfully'
            else:
                response['id:'+str(
                    element)+'_report'] = f'error: the {self.object_name.capitalize()} could not be deleted, please check if ID is correct'
        return Response(response)

    class Meta:
        abstract = True


class CustomSoftDeleteAPIView(generics.UpdateAPIView):

    # TODO ADD BULK UPDATE TO SOFTDELETE ITEMS ON TABLE

    # def __init__(self, *args, **kwargs):
    #     self.object_name = self.__class__.__name__[0:-22]
    #     super(CustomSoftDelete, self).__init__(*args, **kwargs)

    # def delete_inventory_by_pk(self, pk):
    #     try:
    #         self.serializer_class.objects.filter(id=pk)
    #     except ValueError:
    #         return Response({
    #             'error': 'Inventory does not exist'
    #         }, status=status.HTTP_404_NOT_FOUND)

    # def post(self, request):
    #     deletionArray = request.data
    #     response = {}
    #     for element in deletionArray:
    #         if(Inventory.objects.filter(id=element)):
    #             self.delete_inventory_by_pk(pk=element)
    #             response['id:'+str(element) +
    #                      '_report'] = 'error: inventory deleted successfully'
    #         else:
    #             response['id:'+str(
    #                 element)+'_report'] = 'error: the inventory could not be deleted, please check if the id is correct'
    #     return Response(response)
    pass


class CustomRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    # def get_inventory_by_pk(self, pk):
    #     try:
    #         inventory = Inventory.objects.get(pk=pk)
    #     except:
    #         return Response({
    #             'error': 'Inventory does not exist'
    #         }, status=status.HTTP_404_NOT_FOUND)

    # def get(self, request, pk):
    #     inventory = self.get_inventory_by_pk(pk)
    #     serializer = InventorySerializer(inventory)
    #     return Response(serializer.data)

    # def put(self, request, pk):
    #     inventory = Inventory.objects.get(pk=pk)
    #     if request.method == 'PUT':
    #         serializer = InventorySerializer(inventory, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    pass
