#1 Giving Data

result = application.listen_on('GET product detail on product with id')

print(result.id) #should output a "1" for id of Polo

#  get more info about result object 

#2 render new view

#pass 'data' to template html file 'product_detail' in order to render new page.
application.render_view('product_detail.html', data)