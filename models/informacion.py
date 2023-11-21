from odoo import models, fields, api
from odoo.exceptions import ValidationError

class informacion(models.Model):
     _name = 'odoo_basico.informacion'
     _description = 'Exemplo de información'
     _sql_constraints = [('nomeUnico', 'unique(name)', 'Non se pode repetir o nome')]
     _order = "descripcion desc"

     name = fields.Char(required=True, size=20, string="Titulo:")
     descripcion = fields.Text(string="A descripcion:")
     alto_en_cms = fields.Integer(string="Ato en centimetros:")
     largo_en_cms = fields.Integer(string="Largo en centimetros:")
     ancho_en_cms = fields.Integer(string="Ancho en centimetros:")
     peso= fields.Float(digits=(6, 2), default=2.7, string="Peso en kilos")
     densidade = fields.Float(compute="_densidade", store=True, string="Densidade: ")
     literal = fields.Char(store=False)
     volume = fields.Float(compute="_volume", store=True, string="Volume en m3: ")
     autorizado = fields.Boolean(default=True, string="¿Autorizado?")
     sexo_traducido= fields.Selection([("Hombre" , "Home"), ("Mujer" , "Muller"), ("Otro", "Outro")], required=True, string="Sexo")


     @api.depends('alto_en_cms', 'largo_en_cms','ancho_en_cms')
     def _volume(self):
          for rexistro in self:
               rexistro.volume =  (float(rexistro.alto_en_cms) * float(rexistro.largo_en_cms) * float(rexistro.ancho_en_cms))/1000000

     @api.depends('volume', 'peso')
     def _densidade(self):
          for rexistro in self:
               if rexistro.volume != 0:
                    rexistro.densidade = (float(rexistro.peso) / float(rexistro.volume))
               else:
                    rexistro.densidade=0

     @api.onchange('alto_en_cms')
     def _avisoAlto(self):
          for rexistro in self:
               if rexistro.alto_en_cms > 7:
                    rexistro.literal = 'O alto ten un valor posiblemente excesivo %s é maior que 7' % rexistro.alto_en_cms
               else:
                    rexistro.literal = ""

     @api.constrains('peso')  # Ao usar ValidationError temos que importar a libreria ValidationError
     def _constrain_peso(self):  # from odoo.exceptions import ValidationError
          for rexistro in self:
               if rexistro.peso < 1 or rexistro.peso > 4:
                    raise ValidationError('Os peso de %s ten que ser entre 1 e 4 ' % rexistro.name)