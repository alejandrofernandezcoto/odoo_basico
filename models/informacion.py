from odoo import models, fields, api


class informacion(models.Model):
     _name = 'odoo_basico.informacion'
     _description = 'exemplo de odoo basico'

     name = fields.Char(required=True, size=20, string="Titulo:")
     descripcion = fields.Text(string="A descripcion:")
     alto_en_cms = fields.Integer(string="Ato en centimetros:")
     largo_en_cms = fields.Integer(string="Largo en centimetros:")
     ancho_en_cms = fields.Integer(string="Ancho en centimetros:")
     peso= fields.Float(digits=(6, 2), default=2.7, string="Peso en kilos")

