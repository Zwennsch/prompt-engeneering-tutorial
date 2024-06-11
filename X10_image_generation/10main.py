import openai

client = openai.OpenAI()

response = client.images.generate(model="dall-e-3",
                                  prompt="Painting of a wild sea with a young man who is fighting not to drown"
                                  + "and a silent and calm moon in the background. It should be a night lighted only by the moon.",
                                  size="1024x1024",
                                  quality="standard",
                                  n=1,
                                  )

# data[0] gives us the first image
image_url = response.data[0].url

# the response image url is only temporary valid for an hour
print(image_url)

# dall-e-2 might give some more painting style images and dall-e-3 more realistic style images.
