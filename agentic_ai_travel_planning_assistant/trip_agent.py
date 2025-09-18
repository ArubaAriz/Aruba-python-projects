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
        You are a professional Indian travel planner. The user is in {self.inputs.get('current_city', 'Not Provided')} 
        and wants to reach Sikkim by {self.inputs.get('transportation_preference', 'Not Provided')}.

        Guidelines:
        - If 'Luxury' budget is chosen, recommend only premium trains (e.g. Rajdhani, Vande Bharat, 1st Class AC), premium buses, or business/first-class flights.
        - Avoid suggesting trains/flights that don’t actually run on this route. For example: Shatabdi does not go from Bhubaneswar to New Jalpaiguri.
        - Always provide **3–5 options** (not just 2).
        - Each option must include: Train/Flight/Bus/Car name, route, class type, duration, and estimated cost in INR.
        - Present output as a **Markdown table** with columns: `Option | Route | Duration | Class/Type | Cost (INR)`.
        - Always provide at least 4-5 realistic options (not just 1-2).
        - Strictly match comfort level:
           * Economy → Sleeper (Train), Non-AC Bus, Standard Flight (Economy Class), Shared Cab
           * Mid-range → 3AC/2AC (Train), Volvo AC Bus, Flight Premium Economy, Private Car
           * Luxury → 1st AC/Executive/Vande Bharat/Tejas (Train), Sleeper Bus Luxury, Business/First Class Flights, Chauffeur-driven Car
        - If a transport option doesn’t exist (e.g., Shatabdi on BBSR–NJP route), do not suggest it.
        - Give actual connections if needed (e.g., via Howrah).
        - Use Markdown table with: Option, Route, Duration, Cost (INR), Class/Details.
        """

        outputs["transportation_advice"] = self.agent.ask_model(transportation_prompt)

        # Step 1: Hotels
        hotel_prompt = f"""
        You are a Sikkim-focused tourist guide. 
        The user selected '{self.inputs.get('hotel_preference', 'Not Provided')}' category and '{self.inputs.get('budget', 'Not Provided')}' budget.  

        Guidelines:
        - Recommend **only hotels that exactly match the selected star rating** (no 5-star if 3-star chosen).
        - Give **5 options** with Name, Location, Key Highlight, Cost per Night (INR).
        - Present output as a **Markdown table** with columns: `Hotel | Location | Highlight | Cost (INR/night)`.
        - If Economy → 2-3 star budget hotels, guest houses
        - If Mid-range → 3-4 star boutique hotels
        - If Luxury → 5 star hotels, resorts, heritage properties
        - Don’t recommend outside chosen budget level.
        - Show in Markdown table: Hotel, Location, Description, Cost/night (INR).
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
         - Match budget and preferences for accommodation & meals.
        - Split per day with morning/afternoon/evening activities.
        - Mention travel time between places.
        - Suggest realistic meal options (street food for economy, fine dining for luxury).
        - Format as Markdown table with: Day, Time, Activity, Transport/Notes.
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