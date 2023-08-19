import base64
from odoo import models, fields, api
import io
import xlsxwriter

class GeneralLedgerPartner(models.TransientModel):
    _name = 'general.ledger.partner'
    _description = 'General Ledger Report Wizard'

    start_date = fields.Date(string='Start Date')
    end_date = fields.Date(string='End Date')
    journal = fields.Many2one('account.journal', string='Journal')
    partner = fields.Many2one('res.partner', string='Partner')

    def _get_general_ledger_data(self):
        domain = []

        if self.start_date:
            domain.append(('date', '>=', self.start_date))
        if self.end_date:
            domain.append(('date', '<=', self.end_date))
        if self.journal:
            domain.append(('journal_id', '=', self.journal.id))
        if self.partner:
            domain.append(('partner_id', '=', self.partner.id))

        return self.env['account.move.line'].search(domain)

    def generate_report(self):
        data = self._get_general_ledger_data()

        output = io.BytesIO()
        workbook = xlsxwriter.Workbook(output)
        worksheet = workbook.add_worksheet('General Ledger Report')

        # Write date range filter
        date_range_format = workbook.add_format({'bold': True, 'align': 'left'})
        date_range_label = "Date Range Filter: from: {} to: {}".format(
            self.start_date.strftime('%Y-%m-%d') if self.start_date else "N/A",
            self.end_date.strftime('%Y-%m-%d') if self.end_date else "N/A"
        )
        worksheet.write(0, 0, date_range_label, date_range_format)

        # Skip a row for better visual separation
        row = 1

        # Write header row
        header_format = workbook.add_format({'bold': True, 'align': 'center'})
        header_row = ['Date', 'Journal', 'Account', 'Partner', 'Debit', 'Credit']
        for col, label in enumerate(header_row):
            worksheet.write(row, col, label, header_format)

        # Write data rows
        row = 2
        for entry in data:
            worksheet.write(row, 0, entry.date.strftime('%Y-%m-%d'))

            # Write the journal name or a blank cell if no journal
            journal_name = entry.journal_id.name if entry.journal_id else ""
            worksheet.write(row, 1, journal_name)

            # Write the account name or a blank cell if no account
            account_name = entry.account_id.display_name if entry.account_id else ""
            worksheet.write(row, 2, account_name)

            # Write the partner name or a blank cell if no partner
            partner_name = entry.partner_id.name if entry.partner_id else ""
            worksheet.write(row, 3, partner_name)

            # Write the debit amount or a blank cell if no debit
            worksheet.write(row, 4, entry.debit if entry.debit is not None else 0)

            # Write the credit amount or a blank cell if no credit
            worksheet.write(row, 5, entry.credit if entry.credit is not None else 0)

            row += 1

        workbook.close()
        output.seek(0)

        # Encode the XLSX data as base64
        base64_data = base64.b64encode(output.read())

        # Create an attachment and associate it with the wizard
        attachment = self.env['ir.attachment'].create({
            'name': 'General_Ledger_Report.xlsx',
            'type': 'binary',
            'datas': base64_data,
            'res_model': self._name,
            'res_id': self.id,
        })

        # Return an action to display the attachment
        return {
            'type': 'ir.actions.act_url',
            'url': '/web/content/%s?download=true' % attachment.id,
            'target': 'self',
        }
