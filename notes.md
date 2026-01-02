Day 1:
- OCR works on multiple real food labels
- Ingredient names are readable
- Nutrition & instruction text is also captured
- Output is noisy but usable
Day 2:
- Preprocessing alone cannot solve ingredient extraction
- Layout dominance overwhelms OCR unless ROI is selected
- Manual cropping immediately surfaces ingredient text
- Some ingredient regions remain unreadable due to glare/low contrast
- OCR pipeline must include ROI selection + confidence gating
