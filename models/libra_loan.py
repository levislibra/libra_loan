# -*- coding: utf-8 -*-

from odoo import models, fields, api
import time

class LibraLoan(models.Model):
	_name = 'libra.loan'
	# _inherit = ['mail.thread', 'ir.needaction_mixin']
	
	_order = 'id desc'
	# Campos principales
	name = fields.Char('Prestamo')
	sucursal_id = fields.Many2one('libra.entidad', 'Entidad')
	fecha = fields.Date('Fecha', required=True, default=lambda *a: time.strftime('%Y-%m-%d'))
	partner_id = fields.Many2one('res.partner', 'Cliente')
	company_id = fields.Many2one('res.company', 'Empresa', required=False) # default=lambda self: self.env['res.company']._company_default_get('libra.prestamo'))
	state = fields.Selection([('solicitado', 'Solicitado'), ('revision', 'En Revision'), ('autorizado', 'Autorizado'), ('acreditacion_pendiente', 'Acreditacion Pendiente'), ('acreditado', 'Acreditado'), ('precancelado', 'Precancelado'), ('refinanciado', 'Refinanciado'), ('pagado', 'Pagado'), ('incobrable', 'Incobrable'), ('cancelado', 'Cancelado')], string='Estado', default='solicitado')
	currency_id = fields.Many2one('res.currency', "Moneda")