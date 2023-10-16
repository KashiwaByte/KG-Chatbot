from MachineLearning.analyze_question import AnalysisQuestion
from KnowledgeGraph.get_answer import Get_answer
import gradio as gr

if __name__ == "__main__":
    aq = AnalysisQuestion()
    ga = Get_answer()

    question=gr.Textbox(label="请输入你想查询的信息：")

    def answer(question):
        index, params = aq.analysis_question(question)
        answers = ga.get_data(index, params)
      
        qa=""
        qa+="答案："
        print('答案:')
        for ans in answers:
            print(ans[0])
            qa+=str(ans[0]) + "\n"
        



        return qa
    

    ui = gr.Interface(fn=answer, inputs=gr.Textbox(label="请输入你想查询的信息："), outputs="text",title = "<h1 style='font-size: 40px;'><center>知识图谱问答</center></h1>")
    ui.launch()
