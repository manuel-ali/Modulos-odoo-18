from datetime import datetime
from odoo import models, fields, api

class Document(models.Model):
    _name = 'documents.document'
    _description = 'Document'

    name = fields.Char(string='Referencia del Documento')
    cliente = fields.Many2one('clientes.cliente', string='Cliente')
    expediente = fields.Many2one('expedientes.expediente', string='Expediente', ondelete='set null')
    observaciones = fields.Text(string='Observaciones')
    archivo = fields.Binary(string='Archivo')
    name_document = fields.Char(string='Nombre del Documento')
    fecha_subida = fields.Datetime(string='Fecha de Subida')
    fecha_asignacion_cliente = fields.Datetime(string='Fecha de Asignación al Cliente')
    fecha_asignacion_expediente = fields.Datetime(string='Fecha de Asignación del Expediente')
    

    @api.onchange('expediente')
    def _onchange_expediente(self):
        if self.expediente:
            self.fecha_asignacion_expediente = datetime.today()

    @api.onchange('archivo')
    def _onchange_archivo(self):
        if self.archivo:
            self.fecha_subida = datetime.today()
    @api.onchange('cliente')
    def _onchange_cliente(self):
        if self.cliente:
            self.fecha_asignacion_cliente = datetime.today()
