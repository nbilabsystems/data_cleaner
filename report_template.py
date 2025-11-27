# report_template.py

from typing import Any, Dict, List

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)


def _build_cleaning_summary_section(story: List[Any], summary: Dict[str, Any]) -> None:
    styles = getSampleStyleSheet()
    heading = styles["Heading2"]
    body = styles["BodyText"]

    story.append(Paragraph("Cleaning Summary", heading))
    story.append(Spacer(1, 0.2 * cm))

    rows_before = summary["rows_before"]
    rows_after = summary["rows_after"]
    duplicates_removed = summary["duplicates_removed"]
    missing_before = summary["missing_values_before"]
    missing_after = summary["missing_values_after"]

    lines = [
        f"Rows before cleaning: {rows_before}",
        f"Rows after cleaning: {rows_after}",
        f"Duplicate rows removed: {duplicates_removed}",
        f"Missing values before: {missing_before}",
        f"Missing values after: {missing_after}",
    ]

    for line in lines:
        story.append(Paragraph(line, body))

    story.append(Spacer(1, 0.4 * cm))


def _build_global_stats_section(story: List[Any], global_stats: Dict[str, Any]) -> None:
    styles = getSampleStyleSheet()
    heading = styles["Heading2"]
    body = styles["BodyText"]

    story.append(Paragraph("Global Dataset Statistics", heading))
    story.append(Spacer(1, 0.2 * cm))

    lines = [
        f"Number of rows: {global_stats['num_rows']}",
        f"Number of columns: {global_stats['num_columns']}",
        f"Total missing values: {global_stats['total_missing_values']}",
    ]

    for line in lines:
        story.append(Paragraph(line, body))

    story.append(Spacer(1, 0.4 * cm))


def _build_column_stats_table(story: List[Any], columns_stats: List[Dict[str, Any]]) -> None:
    styles = getSampleStyleSheet()
    heading = styles["Heading2"]

    story.append(Paragraph("Column Overview", heading))
    story.append(Spacer(1, 0.2 * cm))

    # Table header
    table_data = [
        ["Column", "Type", "Missing", "Non-null", "Extra"],
    ]

    for col_stats in columns_stats:
        col_name = col_stats["column_name"]
        dtype = col_stats["dtype"]
        missing = col_stats["missing_count"]
        non_null = col_stats["non_null_count"]

        if "mean" in col_stats and col_stats["mean"] is not None:
            extra = f"mean={round(col_stats['mean'], 2)}"
        else:
            extra = f"unique={col_stats.get('num_unique_values', 'N/A')}"

        table_data.append(
            [col_name, dtype, str(missing), str(non_null), extra]
        )

    table = Table(table_data, repeatRows=1)

    table_style = TableStyle(
        [
            ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.black),
            ("ALIGN", (0, 0), (-1, -1), "LEFT"),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("BOTTOMPADDING", (0, 0), (-1, 0), 6),
            ("GRID", (0, 0), (-1, -1), 0.25, colors.grey),
        ]
    )

    table.setStyle(table_style)
    story.append(table)
    story.append(Spacer(1, 0.4 * cm))


def build_pdf_report(
    summary_data: Dict[str, Any],
    output_path: str = "data_cleaning_report.pdf",
    title: str = "Data Cleaning Report",
) -> str:
    """
    Build a simple PDF report summarizing the cleaning process and dataset stats.

    Args:
        summary_data: dict produced by generate_summary()
        output_path: where to write the PDF
        title: title of the report

    Returns:
        The output_path for convenience.
    """
    doc = SimpleDocTemplate(
        output_path,
        pagesize=A4,
        leftMargin=2 * cm,
        rightMargin=2 * cm,
        topMargin=2 * cm,
        bottomMargin=2 * cm,
    )

    styles = getSampleStyleSheet()
    story: List[Any] = []

    # Title
    story.append(Paragraph(title, styles["Title"]))
    story.append(Spacer(1, 0.5 * cm))

    # Sections
    cleaning_summary = summary_data["cleaning_summary"]
    global_stats = summary_data["global_stats"]
    columns_stats = summary_data["columns"]

    _build_cleaning_summary_section(story, cleaning_summary)
    _build_global_stats_section(story, global_stats)
    _build_column_stats_table(story, columns_stats)

    # Build PDF
    doc.build(story)

    return output_path

