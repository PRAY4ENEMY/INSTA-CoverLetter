use std::io::Read; 
use printpdf::*;
use std::fs::File;
use std::io::BufWriter;
use itertools::Itertools;
use glyph_brush_layout::ab_glyph::{Font, FontRef}; 
use glyph_brush_layout::GlyphPositioner; 


fn paragraph(phont: &IndirectFontRef , layer: &PdfLayerReference, glfonts: &[FontRef<'_>; 1], usrtxt: &str, xalign: f32, yalign: f32) {
    let glyphs = glyph_brush_layout::Layout::default().calculate_glyphs(
        glfonts,
        &glyph_brush_layout::SectionGeometry{
            bounds: (mm_to_px(160.0), f32::INFINITY),
            ..Default::default()
        }, 
        &[glyph_brush_layout::SectionText {
            text: usrtxt, 
            scale: glfonts[0].pt_to_px_scale(12.0).unwrap(), 
            font_id: glyph_brush_layout::FontId(0),
        }], 
        );

    assert_eq!(glyphs.len(), usrtxt.chars().count()); 

    let line_start = glyphs
        .iter()
        .enumerate()
        .group_by(|(_, glyph)| glyph.glyph.position.y)
        .into_iter()
        .map(|(y, mut group)| (y, group.next().unwrap().0))
        .collect::<Vec<_>>(); 

    let min = glyphs
        .iter()
        .map(|glyph| glyph.glyph.position.y)
        .fold(f32::INFINITY, |a, b| a.min(b)); 

    let mut iter = line_start.iter().peekable(); 

    loop {

        let Some((y, start)) = iter.next() else {
            break;
        };

        let end = if let Some((_, end)) = iter.peek() {
            *end 
        } else {
            usrtxt.chars().count()
        };

        let line = usrtxt 
            .chars()
            .skip(*start)
            .take(end - start)
            .collect::<String>(); 

        layer.use_text(
            line.trim(), 
            12.0, 
            Mm(xalign.into()), 
            Mm(&yalign.into() + px_to_mm(min) - px_to_mm(*y)), 
            &phont,
            );
    }
}


fn main() {
    let position = "Analyst"; 
    let coname = "Mane"; 
    let location = "Lebanon"; 
    let ntxt = " ";
    let sample = "I hope this letter finds you well. Please accept my resume for consideration as you seek to fill the opening for the asdf role. I think that my skills and experiences would be directly leveraged within this role:";
    let sample3 = "Through my studies of Economics & Political Science, I learned how to take and clean large data sets to examine them for relevant insights. For my capstone project, I looked at the relationship between success in sports and success in admissions. This project required me to take data from multiple sources and put it in panel format. I was able to present my findings to a group of faculty and received high marks for the research.";
    let sample4 = "As a managing member of Xavier’s Newswire, I gained the experience of working with a group of people to achieve the complicated task on editing the school’s weekly newspaper. Putting the paper required attention to detail and clear communication to ensure that the entire team understood what they were responsible for. We were able to win multiple awards with the Ohio News Media Association (ONMA).";
    let sample5 = "I am confident that these experiences and skills, along with my passion to learn, position me to contribute strongly to your team. I hope we can meet and explore this opportunity in more detail.";

    let (doc, page1, layer1) = PdfDocument::new("PDF_Document_title", Mm(212.0), Mm(279.0), "Layer 1");
    let current_layer = doc.get_page(page1).get_layer(layer1);

    // fontdata 

    let font_data = {

        let mut font_file = File::open("../guesser/fonts/TNR-Regular.ttf").unwrap(); 
        let mut font_data = Vec::with_capacity(font_file.metadata().unwrap().len() as usize); 
        font_file.read_to_end(&mut font_data).unwrap();
        font_data
    }; 


    // fontdata loaded  

    let font = doc.add_external_font(font_data.as_slice()).unwrap();

    let gbl_font = glyph_brush_layout::ab_glyph::FontRef::try_from_slice(&font_data).unwrap();
    let gbl_fonts = &[gbl_font]; 

    current_layer.use_text(position.clone(), 12.0, Mm(25.0), Mm(250.0), &font);
    current_layer.use_text(coname.clone(), 12.0, Mm(25.0), Mm(243.0), &font);
    current_layer.use_text(location.clone(), 12.0, Mm(25.0), Mm(236.0), &font);
    current_layer.use_text(ntxt.clone(), 12.0, Mm(25.0), Mm(229.0), &font);

    paragraph(&font, &current_layer, &gbl_fonts, &sample, 25.0, 210.0);
    paragraph(&font, &current_layer, &gbl_fonts, &sample3, 25.0, 170.0);
    paragraph(&font, &current_layer, &gbl_fonts, &sample4, 25.0, 130.0);
    paragraph(&font, &current_layer, &gbl_fonts, &sample5, 25.0, 90.0);

    doc.save(&mut BufWriter::new(
        File::create("test_the_working.pdf").unwrap(),
        ))
        .unwrap();
}


fn px_to_mm(px: f32) -> f64 {
    px as f64 * 3175.0 / 12000.0
}

fn mm_to_px(mm: f64) -> f32 {
    (mm * 12000.0 / 3175.0) as f32
}



