# Generated by Django 2.2.13 on 2020-09-21 05:51

from django.db import migrations, models
import home.blocks
import wagtail.contrib.table_block.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.documents.blocks
import wagtail.images.blocks
import wagtail.snippets.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0109_auto_20200219_1316'),
    ]

    operations = [
        migrations.AddField(
            model_name='custompage',
            name='conditional_js',
            field=models.CharField(blank=True, choices=[('statistical_summary', 'statistical-summary.js')], help_text='Choose a JS script to add only to this page', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='author_group',
            field=models.CharField(blank=True, choices=[('Press Office', 'Press authors'), ('Information Division', 'Information Division authors')], help_text='Not required: Only choose this if you want this author to show up as part an official author group', max_length=255),
        ),
        migrations.AlterField(
            model_name='resourcepage',
            name='related_pages',
            field=wagtail.core.fields.StreamField([('related_pages', wagtail.core.blocks.ListBlock(wagtail.core.blocks.PageChooserBlock())), ('external_page', wagtail.core.blocks.RichTextBlock())], blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='resourcepage',
            name='sections',
            field=wagtail.core.fields.StreamField([('sections', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(required=True)), ('hide_title', wagtail.core.blocks.BooleanBlock(help_text='Should the section title be displayed?', required=False)), ('content', wagtail.core.blocks.StreamBlock([('text', wagtail.core.blocks.RichTextBlock(blank=False, icon='pilcrow', null=False, required=False)), ('documents', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('url', wagtail.core.blocks.URLBlock()), ('media_type', wagtail.core.blocks.CharBlock()), ('text', wagtail.core.blocks.CharBlock())]), icon='doc-empty', template='blocks/section-documents.html')), ('contact_info', wagtail.core.blocks.StructBlock([('label', wagtail.core.blocks.CharBlock(icon='title', required=False)), ('contact_items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('item_label', wagtail.core.blocks.CharBlock(required=False)), ('item_icon', wagtail.core.blocks.ChoiceBlock(choices=[('email', 'Email'), ('fax', 'Fax'), ('hand', 'Hand delivery'), ('phone', 'Phone'), ('mail', 'Mail'), ('github', 'Github'), ('question-bubble', 'Question')])), ('item_info', wagtail.core.blocks.RichTextBlock(required=True))])))])), ('internal_button', wagtail.core.blocks.StructBlock([('internal_page', wagtail.core.blocks.PageChooserBlock()), ('text', wagtail.core.blocks.CharBlock())])), ('external_button', wagtail.core.blocks.StructBlock([('url', wagtail.core.blocks.URLBlock()), ('text', wagtail.core.blocks.CharBlock())])), ('page', wagtail.core.blocks.PageChooserBlock(template='blocks/page-links.html')), ('disabled_page', wagtail.core.blocks.CharBlock(blank=False, help_text='Name of a disabled link', icon='placeholder', null=False, required=False, template='blocks/disabled-page-links.html')), ('document_list', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock()), ('document', wagtail.documents.blocks.DocumentChooserBlock())]), icon='doc-empty', template='blocks/document-list.html')), ('current_commissioners', home.blocks.CurrentCommissionersBlock()), ('fec_jobs', home.blocks.CareersBlock()), ('mur_search', home.blocks.MURSearchBlock()), ('audit_search', home.blocks.AuditSearchBlock()), ('table', wagtail.contrib.table_block.blocks.TableBlock(table_options={'renderer': 'html'})), ('custom_table', wagtail.core.blocks.StructBlock([('custom_table', wagtail.core.blocks.StreamBlock([('title', wagtail.core.blocks.CharBlock(required=False)), ('table_intro', wagtail.core.blocks.RichTextBlock(required=False)), ('table', wagtail.contrib.table_block.blocks.TableBlock(table_options={'colHeaders': True, 'height': 108, 'language': 'en', 'renderer': 'html', 'rowHeaders': True, 'startCols': 6, 'startRows': 7})), ('footnote', wagtail.core.blocks.CharBlock(required=False))]))])), ('html', wagtail.core.blocks.RawHTMLBlock()), ('reporting_example_cards', wagtail.core.blocks.StructBlock([('card_width', wagtail.core.blocks.ChoiceBlock(choices=[(2, '1/2'), (3, '1/3')], help_text='Control the width of the cards')), ('cards', wagtail.core.blocks.ListBlock(wagtail.core.blocks.PageChooserBlock(), icon='doc-empty'))])), ('contribution_limits_table', wagtail.snippets.blocks.SnippetChooserBlock('home.EmbedTableSnippet', icon='table', template='blocks/embed-table.html')), ('image', wagtail.images.blocks.ImageChooserBlock()), ('example_image', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(required=False)), ('caption', wagtail.core.blocks.RichTextBlock(required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(required=True))])), ('summary_segment', wagtail.core.blocks.StructBlock([('latest_available_segment', wagtail.core.blocks.ChoiceBlock(choices=[('6', '6 Month'), ('12', '12 Month'), ('15', '15 Month'), ('18', '18 Month'), ('21', '21 Month'), ('24', '24 Month')], help_text='Choose latest available segment'))]))])), ('aside', wagtail.core.blocks.StreamBlock([('title', wagtail.core.blocks.CharBlock(icon='title', required=False)), ('document', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('url', wagtail.core.blocks.URLBlock()), ('media_type', wagtail.core.blocks.CharBlock()), ('text', wagtail.core.blocks.CharBlock())])), ('link', wagtail.core.blocks.StructBlock([('link_type', wagtail.core.blocks.ChoiceBlock(choices=[('calculator', 'Calculator'), ('calendar', 'Calendar'), ('record', 'Record'), ('search', 'Search')], help_text='Set an icon', icon='link', required=False)), ('url', wagtail.core.blocks.URLBlock()), ('text', wagtail.core.blocks.CharBlock(required=True)), ('coming_soon', wagtail.core.blocks.BooleanBlock(required=False))]))], icon='placeholder', required=False, template='blocks/section-aside.html'))]))], blank=True, null=True),
        ),
    ]
