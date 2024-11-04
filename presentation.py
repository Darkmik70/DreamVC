from dreamvoice import DreamVoice

prompt1 = "Authoritative sounding person, who is gender-ambiguous and adult."
prompt2 = "A teenage girl's voice that is smooth, warm, and attractive, perfect for captivating storytelling."
prompt3 = "A mature male voice, bright and engaging, good for client and public interaction."

# End-to-end mode (DreamVC)
# Initialize DreamVoice in end-to-end mode with CUDA device
dreamvoice = DreamVoice(mode='end2end', device='cuda')


# Provide the path to the content audio and generate the converted audio
gen_end2end, sr = dreamvoice.genvc('samples/son_house_john.wav', prompt1)
# Save the converted audio
dreamvoice.save_audio('results/son_house_converted.wav', gen_end2end, sr)

# # Provide the path to the content audio and generate the converted audio
# gen_end2end, sr = dreamvoice.genvc('samples/witcher_pl.wav', prompt2)
# # Save the converted audio
# dreamvoice.save_audio('results/witcher_converted.wav', gen_end2end, sr)

# # Provide the path to the content audio and generate the converted audio
# gen_end2end, sr = dreamvoice.genvc('samples/sara_walker.wav', prompt3)
# # Save the converted audio
# dreamvoice.save_audio('results/sara_walker_converted.wav', gen_end2end, sr)

