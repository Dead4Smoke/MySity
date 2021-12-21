# if table1:
#       table_objects = []
#       table_objects.append({"value": table1.ObjectA})
#       table_objects.append({"value": table1.ObjectB})
#       table_objects.append({"value": table1.ObjectG})
#       table_objects.append({"value": table1.ObjectV})
#       doc = DocxTemplate("./base/static/base/dock/TAB0.docx")
#       context = {
#             "tbl1": table_objects
#             }
#       doc.render(context)
#       b = BytesIO()
#       doc.save(b)
#       b.seek(0)
#       return b
#    return False