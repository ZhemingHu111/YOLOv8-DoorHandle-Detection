from args import get_opts
from dataset import prepare_data
from model import get_model
from trainer import run_train

def main():
    opts = get_opts()
    
    prepare_data(opts)
    
    model = get_model(opts['model_type'])
    
    run_train(model, opts)

if __name__ == "__main__":
    main()