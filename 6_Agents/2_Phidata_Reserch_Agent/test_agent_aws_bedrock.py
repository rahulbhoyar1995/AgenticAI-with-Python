from phi.agent import Agent, RunResponse
from phi.model.aws.claude import Claude
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

agent = Agent(
    model=Claude(id="anthropic.claude-3-5-sonnet-20240620-v1:0"),
    markdown=True
)
#Get the response in a variable
run: RunResponse = agent.run("Write 100 words essay on Artificial Intelligence")
print(run.content)

