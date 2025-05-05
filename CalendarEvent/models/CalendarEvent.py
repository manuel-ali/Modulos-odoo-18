from odoo import models, fields
from odoo.exceptions import UserError
from datetime import datetime
import pytz
import base64

class CalendarEvent(models.Model):
    _inherit = 'calendar.event'

    expediente_id = fields.Many2one('expedientes.expediente', string='Expediente Asociado')
    observaciones = fields.Text(string='Observaciones')

    def action_export_ics(self):
        if not self:
            raise UserError("No se han seleccionado eventos para exportar.")

        cal_lines = [
            "BEGIN:VCALENDAR",
            "VERSION:2.0",
            "PRODID:-//Odoo Calendar Export//ES"
        ]

        tz = self.env.user.tz or 'UTC'
        tzinfo = pytz.timezone(tz)

        for event in self:
            start_utc = event.start.astimezone(tzinfo).strftime('%Y%m%dT%H%M%S')
            stop_utc = event.stop.astimezone(tzinfo).strftime('%Y%m%dT%H%M%S')

            cal_lines.extend([
                "BEGIN:VEVENT",
                f"SUMMARY:{event.name or 'Sin título'}",
                f"DTSTART;TZID={tz}:{start_utc}",
                f"DTEND;TZID={tz}:{stop_utc}",
                f"DESCRIPTION:{event.observaciones or ''}",
                f"UID:{event.id}@odoo",
                "END:VEVENT"
            ])

        cal_lines.append("END:VCALENDAR")

        ics_data = '\n'.join(cal_lines)
        ics_file = self.env['ir.attachment'].create({
            'name': 'eventos.ics',
            'datas': base64.b64encode(ics_data.encode('utf-8')),
            'type': 'binary',
            'res_model': 'calendar.event',
            'res_id': self.ids[0],
            'mimetype': 'text/calendar'
        })

        return {
            'type': 'ir.actions.act_url',
            'url': f"/web/content/{ics_file.id}?download=true",
            'target': 'new',
        }
