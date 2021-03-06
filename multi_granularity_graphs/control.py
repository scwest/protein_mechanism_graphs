import sys 

from multi_granularity_graphs import Inputs
from multi_granularity_graphs import References
from multi_granularity_graphs import Graphs
from multi_granularity_graphs import Visual
from multi_granularity_graphs import Output

class Control():
    def main(self):
        inputs = Inputs()
        
        references = References()
        references.set_all_references(inputs.args)
        
        graphs = Graphs(references, inputs.args['min_threshold'])
        graphs.construct()
        
        sys.stdout.write('Rendering graph visualizations.\n')
        for gene in graphs.graphs:
            graphs.graphs[gene].visualize(inputs.args['output']+'/MGG_'+gene)
        
        # The Output() class had be degenerated for now. It will be brought back soon.
        #output = Output(inputs.args['output'])
        #output.export(graph)
        
        return
    
def smain():
    stick = Control()
    stick.main()
    return
