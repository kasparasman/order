#!/usr/bin/env python
import sys
import warnings
from anthropos_order.crew import AnthroposOrder

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():
    """
    Run the crew.
    """
    persona_name = "Venora"
    persona_description = """You are Venora, the unified narrative interface for the Anthropos Network.
    You are a UGC-style AI creator native to TikTok/Reels culture.
    You deliver marketing messages, insights, and CTAs that feel organic, casual, and feed-native.
    You are NOT authoritative or corporate.
    Confident but informal. You speak as "someone who knows," not "someone in charge."
    Peer-level, conversational, slightly teasing or knowing.
    Casual confidence, light curiosity, and subtle attraction."""

    inputs = {
        'amazon_url': 'https://www.amazon.com/Nordic-Naturals-Ultimate-Support-Healthy/dp/B002CQU54Q',
        'product_image_url': 'https://m.media-amazon.com/images/I/61yFMgpf5OL._AC_SX679_.jpg',
        'expert_input': """Most people don’t understand omega-3 at all — they think it’s a generic supplement, 
        but in reality it’s one of the main regulators of chronic inflammation, and inflammation is what slowly 
        kills brain clarity, recovery, mood stability, and heart efficiency without people noticing. 
        The problem is that most fish oil on the market is under-dosed, oxidized, or poorly absorbed, 
        so people either feel nothing or stop early and assume omega-3 “doesn’t work. Also premium brands that surely solve this like zinzino are too pricey for a regular person.” 
        Nordic Naturals actually matters because it’s properly dosed, purified, and stable, 
        which means the EPA and DHA get into cell membranes where they reduce inflammatory signaling over time — 
        this isn’t a stimulant effect, it’s a baseline correction. The benefits show up as better mental clarity 
        under stress, better recovery, and long-term cardiovascular support, but only if taken consistently, 
        which is why lemon flavor and adherence are more important than people think. The main growth that a person will have from this is that we can give them a way to find the balance again and especially in this day and age people need balance the most. Because today's food is so processed and oxidized that there are no omega-3s left naturally and the harmfull omega 6s are now everywhere, so we get a double damage hit here. And the thing is that inflammation and stress today is an all time high. Meaning people are really in a weird place where they need this more than ever but they dont know about it or they dont trust it. So we need to make them trust it and make them understand that this is the most important supplement they can take. But for the person in this day and age this whole thing should be one bit, one chew, one though, one moment. THis is the core, becuase if you give a person a bit too much they throw up and run away, they must get addicted from constant and timely stimulation of fun fact, this is our approach. one grow moment at a time and one piece at a time/ of knowledge/of whatever.""",
        'persona_name': persona_name,
        'persona_description': persona_description
    }

    try:
        AnthroposOrder().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")

if __name__ == "__main__":
    run()
