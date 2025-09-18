import streamlit as st
from trip_agent import TripCrew
from dotenv import load_dotenv
import os  
import io
import pandas as pd
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet 

load_dotenv()

def generate_pdf(inputs, crew_output):
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer)
    styles = getSampleStyleSheet()
    elements = []

    # Title
    elements.append(Paragraph("Sikkim Travel Planning Assistant", styles["Title"]))
    elements.append(Spacer(1, 12))

    # Add each section
    for section, content in crew_output.items():
        elements.append(Paragraph(section.replace("_", " ").title(), styles["Heading2"]))
        elements.append(Paragraph(str(content).replace("\n", "<br/>"), styles["Normal"]))
        elements.append(Spacer(1, 12))

    doc.build(elements)
    buffer.seek(0)
    return buffer


def main():
    st.set_page_config(page_title="Sikkim Travel Planner", page_icon="🗺️", layout="wide")

    # Title with subtitle
    st.title(" Sikkim Travel Planning Assistant")
    st.markdown("Plan your perfect trip to the **Land of Monasteries & Mountains** ")

    # Sidebar
    with st.sidebar:
        st.header(" Trip Preferences")
        current_city = st.text_input(" Enter Your Current City")
        transportation_preference = st.selectbox(" Preferred Mode of Transportation", ["Car", "Bus", "Train", "Flight"])
        travel_type = st.selectbox(" Travel Type", ["Leisure", "Business", "Adventure", "Cultural"])
        interests = st.multiselect(" Interests", ["History", "Nature", "Food", "Art", "Shopping", "Sports", "Nightlife"])
        season = st.selectbox(" Season", ["Spring", "Summer", "Autumn", "Winter"])
        days = st.number_input(" Number of Days", min_value=1, max_value=30, value=7)
        nights = st.number_input(" Number of Nights", min_value=0, max_value=30, value=6)
        duration = f"{days} Days + {nights} Nights"
        hotel_preference = st.selectbox(" Hotel Preference", ["Normal", "3 star", "5 star", "Guest House"])
        budget = st.selectbox(" Total Budget Range", ["Economy", "Mid-range", "Luxury"])

    # Main Button
    if st.button(" Generate Travel Plan", use_container_width=True):
        inputs = {
            "current_city": current_city,
            "transportation_preference": transportation_preference,
            "travel_type": travel_type,
            "interests": interests,
            "season": season,
            "duration": duration,
            "hotel_preference": hotel_preference,
            "budget": budget
        }

        crew = TripCrew(inputs)

        with st.spinner(" Crafting your travel experience..."):
            try:
                crew_output = crew.run()

                # Sections with expanders
                with st.expander(" Transportation Options", expanded=True):
                    st.markdown("### Travel Options")
                    st.text_area("AI Suggested Routes", crew_output.get("transportation_advice", "No data available"), height=200)


                with st.expander(" Recommended Hotels"):
                    st.markdown("### Hotel Recommendations")
                    hotels_raw = crew_output.get("hotel_advice", "No data available")
                    for hotel in hotels_raw.split("\n\n"):
                        st.markdown(
                            f"""
                            <div style="padding:10px; border:1px solid #ddd; border-radius:10px; margin-bottom:12px; background:#f9f9f9;">
                                {hotel}
                            </div>
                            """, unsafe_allow_html=True
                        )

                with st.expander(" Recommended Cities to Visit"):
                    st.write(crew_output.get("city_selection", "No data available"))

                with st.expander(" Destination Insights"):
                    st.write(crew_output.get("city_research", "No data available"))

                with st.expander(" Detailed Itinerary"):
                    st.write(crew_output.get("itinerary", "No data available"))

                with st.expander(" Budget Breakdown"):
                    st.write(crew_output.get("budget_breakdown", "No data available"))

                st.success("✅ Trip plan generated successfully! Pack your bags and enjoy Sikkim 🎒✨")
                
                pdf_buffer = generate_pdf(inputs, crew_output)
                st.download_button(
                label="📄 Save Travel Plan as PDF",
                data=pdf_buffer,
                file_name="sikkim_travel_plan.pdf",
                mime="application/pdf",
                use_container_width=True
            )


            except Exception as e:
                st.error(f"⚠️ Error generating travel plan: {e}")

if __name__ == "__main__":
    main()
