class TestCustomUtils:
    @classmethod
    def fix_fk_assertion(cls, data, content, fk_array):
        '''This method equals data FK (response to DB test) to content
         FK (factory.build() return). It's necessary, because factory.build() generates FK fields with values different 
         from the response, causing error'''
        for fk in fk_array:
            content[fk] = data[fk]

    @classmethod
    def fix_id_assertion(cls, data, content):
        '''This method equals data id (response to DB test) to content
         FK (factory.build() return). It's necessary because id is given by DB 
         when the objec is created, so the object returned by factory,build() miss this attribute'''
        content['id'] = data['id']
