'use strict';

var $ = require('jquery');

var tables = require('../modules/tables');
var columns = require('../modules/columns');

var donationTemplate = require('../templates/receipts.hbs');

$(document).ready(function() {
  var $table = $('#results');
  new tables.DataTable($table, {
    autoWidth: false,
    title: 'Individual contributions',
    path: ['schedules', 'schedule_a'],
    query: { is_individual: true, sort_nulls_last: false },
    columns: columns.individualContributions,
    paginator: tables.SeekPaginator,
    order: [[4, 'desc']],
    useFilters: true,
    useExport: true,
    rowCallback: tables.modalRenderRow,
    error400Message:
      '<p>When searching multiple time periods, choose one or more fields: recipient name or ID, contributor name or ID, city, ZIP code, occupation or employer, or image number.</p>',
    callbacks: {
      afterRender: tables.modalRenderFactory(donationTemplate)
    }
  });
});
