import time

out_dir = 'out-haiku'
eval_interval = 5
eval_iters = 40
wandb_log = True # feel free to turn on
wandb_project = 'haiku'
wandb_run_name = 'test3'

dataset = 'haiku'
init_from = 'gpt2-large' # this is the largest GPT-2 model

# only save checkpoints if the validation loss improves
always_save_checkpoint = False

# the number of examples per iter:
# 1 batch_size * 32 grad_accum * 1024 tokens = 32,768 tokens/iter
# shakespeare has 301,966 tokens, so 1 epoch ~= 9.2 iters
# haiku has 2,301,966 tokens, so 1 epoch ~= 70 iters * 10 number of iterations
batch_size = 1
gradient_accumulation_steps = 32
max_iters = 10000

# finetune at constant LR
learning_rate = 1e-6
decay_lr = True
warmup_iters = 200#max_iters/10
lr_decay_iters = max_iters 
min_lr = learning_rate/10

compile=True
