import pandas as pd


def lift(dataset, ant_field, ant_value, cons_field, cons_value):
    """ calculate lift given a dataset and rule as defined by the given values """
    all_count = dataset.apply(pd.value_counts)
    cons_count = all_count.get(cons_field)
    ant_count = all_count.get(ant_field)
    
    given_count = test_df.drop(
        dataset[dataset[ant_field] != ant_value].index).apply(pd.value_counts)
    
    
    conf = given_count.get(cons_field)[cons_value] / ant_count[ant_value]
    prob_overall = cons_count[cons_value] / len(dataset)
    
    return conf / prob_overall


if __name__ == '__main__':
    test_set = [[0,0],[0,0],[0,1],[0,0],[1,1],[1,0],[1,1]]
    test_df = pd.DataFrame(test_set, columns=['antecedent','consequent'])
    lift(dataset=test_df, 
         ant_field="antecedent", 
         ant_value=1,
         cons_field='consequent', 
         cons_value=1)


# lift() # should be 1.56 repeating

