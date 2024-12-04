import json
from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import parser_classes, renderer_classes

from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework_xml.parsers import XMLParser
from rest_framework_xml.renderers import XMLRenderer


@csrf_exempt
@api_view(['POST', ])
@parser_classes([XMLParser])
@renderer_classes([XMLRenderer])
def plotShape(request):

    if request.method == 'POST':
        # loads decoded body of request
        body_data = json.loads(request.body.decode('utf-8'))
        # takes in geometry attribute of request JSON
        geom_data = body_data['geometry']
        plane = body_data['plane']  # takes in plane attribute of request JSON

        geom_length = len(geom_data)

        print("""
            xml
            <svg baseProfile="full" height="100%" version="1.1" viewBox="-450,-109,900,618" width="100%" xmlns="http://www.w3.org/2000/svg">
            <defs/>    
        """
              )  # trying to figure out how to plot for SVG after using print statements

        if plane == 'XY':
            """ If plane XY is sent in request body """
            for i in range(geom_length):
                # parsing out values of x1 to be used as values of X-coordinate in XML
                x1 = geom_data[i]['x1']
                # parsing out values of y1 to be used as values of Y-coordinate in XML
                y1 = geom_data[i]['y1']

                # parsing out values of x2 to be used as values of X-coordinate in XML
                x2 = geom_data[i]['x2']
                # parsing out values of y2 to be used as values of Y-coordinate in XML
                y2 = geom_data[i]['y2']

                height = y2 - y1  # obtaining the height of the figure
                width = x2 - x1  # obtaining the width of the figure

                line_to_be_printed = '<rect fill="gray" height="{}" stroke="black" width="{}" x="{}" y="{}"/>'.format(
                    height, width, x1, y1)

                print(line_to_be_printed)

        if plane == 'XZ':
            """ If plane XZ is sent in request body """
            for i in range(geom_length):
                # parsing out values of x1 to be used as values of X-coordinate in XML
                x1 = geom_data[i]['x2']
                # parsing out values of y1 to be used as values of Y-coordinate in XML
                z1 = geom_data[i]['z1']

                # parsing out values of x2 to be used as values of X-coordinate in XML
                x2 = geom_data[i]['x1']
                # parsing out values of y2 to be used as values of Y-coordinate in XML
                z2 = geom_data[i]['z2']

                height = z2 - z1  # obtaining the height of the figure
                width = x1 - x2  # obtaining the width of the figure

                line_to_be_printed = '<rect fill="gray" height="{}" stroke="black" width="{}" x="{}" y="{}"/>'.format(
                    height, width, x1, z1)

                print(line_to_be_printed)

        if plane == 'YZ':
            """ If plane YZ is sent in request body """
            for i in range(geom_length):
                # parsing out values of x1 to be used as values of X-coordinate in XML
                y1 = geom_data[i]['y2']
                # parsing out values of y1 to be used as values of Y-coordinate in XML
                z1 = geom_data[i]['z2']

                # parsing out values of x2 to be used as values of X-coordinate in XML
                y2 = geom_data[i]['y1']
                # parsing out values of y2 to be used as values of Y-coordinate in XML
                z2 = geom_data[i]['z1']

                height = y1 - y2  # obtaining the height of the figure
                width = z1 - z2  # obtaining the width of the figure

                line_to_be_printed = '<rect fill="gray" height="{}" stroke="black" width="{}" x="{}" y="{}"/>'.format(
                    height, width, x1, z1)

                print(line_to_be_printed)

        # trying to figure out how to plot for SVG after using print statements
        print('</svg>')
    try:
        return Response({'success': 1}, status=200)

    except Exception as e:
        return JsonResponse({'the error is': str(e)}, status=403)
