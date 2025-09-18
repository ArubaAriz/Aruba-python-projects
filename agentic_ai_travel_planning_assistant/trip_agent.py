import os
from groq import Groq

class TripAgent:
    def __init__(self, model="llama-3.1-8b-instant"):
        api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            raise ValueError(" Missing GROQ_API_KEY environment variable")
        self.client = Groq(api_key=api_key)
        self.model = model

    def ask_model(self, prompt: str) -> str:
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content


class TripCrew:
    def __init__(self, inputs):
        self.inputs = inputs
        self.agent = TripAgent()

    def run(self):
        outputs = {}
        
        
        # Step 0: Transportation
        transportation_prompt = f"""
        The user is currently in {self.inputs.get('current_city', 'Not Provided')}.
        They want to travel to Sikkim by {self.inputs.get('transportation_preference', 'Not Provided')}.
        Suggest the best way to reach Sikkim from this city, step by step.
        Include:
        - Recommended route
        - Approximate travel time
        - Estimated cost (in INR)
        - Practical travel tips
        """
        outputs["transportation_advice"] = self.agent.ask_model(transportation_prompt)

        # Step 1: Hotels
        hotel_prompt = f"""
        You are a Sikkim-focused tourist guide.
        Based on the hotel preference '{self.inputs.get('hotel_preference', 'Not Provided')}'
        and budget '{self.inputs.get('budget', 'Not Provided')}',
        suggest 5 hotels in Sikkim.
        For each include:
        - Name
        - Location
        - Short description
        - Approximate cost per night (INR)
        """
        outputs["hotel_advice"] = self.agent.ask_model(hotel_prompt)

        # Step 2: Recommended Cities
        city_prompt = f"""
        You are a Sikkim travel assistant.
        Recommend 3 must-visit places in Sikkim for:
        - Travel Type: {self.inputs['travel_type']}
        - Interests: {', '.join(self.inputs['interests'])}
        - Season: {self.inputs['season']}
        - Duration: {self.inputs['duration']}
        - Budget: {self.inputs['budget']}
        Write in bullet points with 2 sentences per place.
        """
        outputs["city_selection"] = self.agent.ask_model(city_prompt)

        # Step 3: Destination Insights
        research_prompt = """
        For the recommended Sikkim destinations, provide:
        - Top 5 monasteries/attractions
        - Local cuisine highlights
        - Cultural etiquette
        - Recommended accommodation areas
        - Transportation tips
        Format in Markdown with headings.
        """ 
        outputs["city_research"] = self.agent.ask_model(research_prompt)

        # Step 4: Itinerary
        itinerary_prompt = f"""
        Create a detailed {self.inputs['duration']} itinerary for the selected places in Sikkim.
        Include:
        - Daily schedule with time slots
        - Activity sequencing
        - Transportation between locations with estimated cost
        - Meal planning suggestions with estimated costs
        Format as a Markdown table.
        """
        outputs["itinerary"] = self.agent.ask_model(itinerary_prompt)

        # Step 5: Budget Breakdown
        budget_prompt = f"""
        Create a budget plan for {self.inputs['budget']} style travel in Sikkim.
        Duration: {self.inputs['duration']}
        Include:
        - Accommodation costs
        - Transportation expenses
        - Activity fees
        - Meal costs
        - Emergency funds
        - give a realistic total budget estimate
        Format as a Markdown table with totals in INR.
        """
        outputs["budget_breakdown"] = self.agent.ask_model(budget_prompt)

        return outputs